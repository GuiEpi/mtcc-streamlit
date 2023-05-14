from mako.template import Template
from datetime import datetime
from deezer import Album
import deezer


class Pres:
    def __init__(
        self,
        research: str = None,
        nfo_properties: dict = None,
        upload_infos: dict = None,
    ) -> None:
        self.research = research
        self.nfo_properties = nfo_properties
        self.upload_infos = upload_infos
        self.properties = None
        self.client = deezer.Client()
        self.torrent_name = None
        self.template = Template(filename="./templates/pres.mako")

    def __str__(self):
        return self.template.render(
            album=self.properties, nfo=self.nfo_properties, upload=self.upload_infos
        )

    def search(self) -> None:
        if self.research:
            # need to be implemented
            print("Comming soon...")
            pass
        else:
            result = self.client.search(self.nfo_properties["album_performer"])
            for data in result[:20]:
                album = data.get_album()
                if self.nfo_properties["album"] == album.title:
                    self.properties = album
                    self.torrent_name = f"[{album.genres[0].name}] {album.artist.name} - {album.title} ({album.record_type.upper()}) [{album.release_date.strftime('%Y')}] [{self.nfo_properties['format']}, {self.nfo_properties['bit_depth']}-{int(self.nfo_properties['sampling_rate'] / 1000)}] KK"
                    break
