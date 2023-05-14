from datetime import datetime, timedelta
from mako.template import Template
from pymediainfo import MediaInfo
import utils
import json


class Nfo:
    def __init__(self, settings: dict) -> None:
        self.tracks = []
        self.properties = {
            "track_name_maxlen": 0,
            "playing_time": "",
            "total_size": 0,
        }
        self.settings = settings
        self.template = Template(filename="./templates/nfo.mako")
        self.filename = "mtcc_no_name"

    def __str__(self):
        return self.template.render(
            tracklist=self.tracks, album=self.properties, settings=self.settings
        )

    def get_tagfiles(self, files) -> list[dict]:
        tag_files = []
        audio_properties = {}
        for file in files:
            if "audio" in file.type:
                tag_file = MediaInfo.parse(file)
                tag_file_json = json.loads(tag_file.to_json())
                tag_files.append(tag_file_json["tracks"][0])
                if not audio_properties:
                    audio_properties = tag_file_json["tracks"][0]
                    audio_properties.update(tag_file_json["tracks"][1])
        self.properties.update(audio_properties)
        return tag_files

    def parse(self, files) -> None:
        tag_files = self.get_tagfiles(files)
        playing_time = []

        for tag_file in tag_files:
            track = {"track_name_len": 0}

            for tag_properties in tag_file:
                track[tag_properties] = tag_file[tag_properties]

            if "track_name_position" not in tag_file:
                print(f"[ERROR] track_name_position not found")

            track["track_name_len"] = len(track["track_name"])

            longest_trackname = max(
                [self.properties["track_name_maxlen"], track["track_name_len"]]
            )
            self.properties["track_name_maxlen"] = longest_trackname
            self.properties["total_size"] += track["file_size"]

            # fix time error with the "duration" property
            time_obj = datetime.strptime(track["other_duration"][4], "%H:%M:%S.%f")
            track["duration"] = time_obj.strftime("%M:%S")
            playing_time.append(track["duration"])

            self.tracks.append(track)

        self.tracks.sort(key=lambda k: int(k["track_name_position"]))

        if len(self.tracks) == 0:
            print("[ERROR] No tracks found")

        self.properties.update(self.tracks[0])
        self.properties["total_size"] = utils.convert_size(
            self.properties["total_size"]
        )
        self.properties["playing_time"] = self.__get_playing_time(playing_time)
        self.filename = (
            f"{self.properties['album']} [{self.properties['recorded_date']}]"
        )

    def __get_playing_time(self, playing_times: dict[str]) -> str:
        time_deltas = [
            timedelta(minutes=int(time.split(":")[0]), seconds=int(time.split(":")[1]))
            for time in playing_times
        ]
        total_time_delta = sum(time_deltas, timedelta())
        total_seconds = int(total_time_delta.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        total_time_formatted = f"{minutes:02}:{seconds:02}"

        return total_time_formatted
