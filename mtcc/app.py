from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st
from nfo import Nfo
from pres import Pres
from deezer import Album
import config
import utils
import re

st.set_page_config(
    page_title="mtcc",
    page_icon="📋",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/GuiEpi/mtcc",
        "Report a bug": "https://github.com/GuiEpi/mtcc/issues",
        "About": "# mtcc - Music Torrent Content Creator\nhttps://github.com/GuiEpi/mtcc",
    },
)


def display_header() -> None:
    mttc_nfo_builder, mtcc_pres, _ = st.columns(3)
    with mttc_nfo_builder:
        st.image(f"{config.MTCC_LOGO_LINK}/mtcc_nfo_builder.png")
    with mtcc_pres:
        st.image(f"{config.MTCC_LOGO_LINK}/mtcc_pres.png")
    st.title("Welcome to the mtcc tool panel")
    st.divider()
    st.write(
        "##### mtcc is a user-friendly tool designed for content creators to easily upload a music torrent."
    )


def display_settings() -> dict:
    with st.sidebar:
        st.title("Settings")
        ripper = st.text_input("Ripper", config.NFO_RIPPER)
        uploader = st.text_input("Uploader", config.NFO_UPLOADER)
        options = (banner for banner in config.PRES_BANNERS)
        selected_banner = st.selectbox("Choose your banner theme", options)
        for banner in config.PRES_BANNERS:
            with st.expander(banner):
                for file_name in config.PRES_BANNERS_FILES_NAME:
                    st.image(f"{config.PRES_BANNERS[banner]}/{file_name}")
        ygg_link = st.text_input("Ygg profile url", config.PRES_YGG_LINK)
        ygg_tag = st.text_input("Ygg uploader tag", config.PRES_YGG_TAG)

    return {
        "ripper": ripper,
        "uploader": uploader,
        "nfo_name": config.NFO_NAME,
        "nfo_version": config.NFO_VERSION,
        "banner_theme": config.PRES_BANNERS[selected_banner],
        "ygg_link": ygg_link,
        "ygg_tag": ygg_tag,
        "mtcc_link": config.MTCC_LINK,
    }


def extract_files(tab) -> UploadedFile:
    files = st.file_uploader(
        "Upload your album/single here.",
        accept_multiple_files=True,
        type=["wav", "mp3", "flac", "jpg", "jpeg", "png"],
        key=tab,
    )

    if not (files):
        st.error("A file is needed.")

    return files


def display_album(albums: list[Album]):
    selected_album = None
    album_chunks = [albums[i : i + 3] for i in range(0, len(albums), 3)]
    cols = st.columns(3)

    for chunk, col in zip(album_chunks, cols):
        for album in chunk:
            with col:
                with st.expander(album.title):
                    st.header(album.title)
                    st.text(album.artist.name)
                    st.image(album.cover_medium)
                    if st.button("Select", key=album.id):
                        selected_album = album
    if selected_album:
        return selected_album


def search_album(tab) -> str:
    research = st.text_input("Search album", key=tab)
    if not research:
        st.error("A research is needed.")
    return research


def display_torrent_contents(pres: Pres) -> None:
    st.write("#### Torrent name")
    st.code(pres.torrent_name)
    st.write("#### Torrent description")
    st.code(str(pres), language="bbcode")


def get_upload_infos(files: UploadedFile) -> dict:
    total_size = 0
    for file in files:
        total_size += file.size
    return {
        "nb_files": len(files),
        "total_size": utils.convert_size(total_size),
    }


def display_input_widgets() -> tuple[str, str, int, int, int]:
    codec = st.selectbox("Codec", ["MP3", "FLAC (16 bit)", "FLAC (24 bit)", "WAV"])
    if codec != "MP3":
        frequency = st.selectbox(
            "Frequency", ["44.1 kHz", "48 kHz", "96 kHz", "176.4 kHz", "192 kHz"]
        )
    else:
        frequency = "44.1 kHz"
    default_bitrate = 0
    if re.search(r"\b\d+\b", codec):
        default_bitrate = (
            float(re.findall(r"\d+\.\d+", frequency)[0])
            * 2
            * int(re.findall("[0-9]+", codec)[0])
        )
    audio_bitrate = st.number_input("Audio bitrate (kb/s)", value=default_bitrate)
    nb_file = st.number_input("No. of files", value=0)
    total_size = st.number_input("Total size (Mo)", value=0)

    return codec, frequency, audio_bitrate, nb_file, total_size


def create_dict_from_input(
    codec: str, frequency: str, audio_bitrate: int, nb_file: int, total_size: int
) -> tuple[dict, dict]:
    technical_details = {
        "format": codec.split()[0],
        "bit_depth": str(re.findall("[0-9]+", codec)[0])
        if re.search(r"\b\d+\b", codec)
        else audio_bitrate,
        "other_bit_depth": [codec],
        "audio_bitrate": str(audio_bitrate),
        "other_sampling_rate": [frequency],
        "sampling_rate": int(float(re.findall(r"\d+\.\d+", frequency)[0]) * 1000),
    }
    infos_download = {
        "nb_files": nb_file,
        "total_size": total_size,
    }
    return technical_details, infos_download


def extract_information():
    st.header("Informations")
    st.text(
        "Give informations about upload before try to find album.\nIf you also have settings to change, you should do it now."
    )
    codec, frequency, audio_bitrate, nb_file, total_size = display_input_widgets()
    return create_dict_from_input(codec, frequency, audio_bitrate, nb_file, total_size)


def display_mtcc(settings: dict) -> None:
    st.header("mtcc")
    st.write(
        "###### mtcc is the best solution, it combines mtcc Nfo Builder and mtcc PRES so you can do both from the upload."
    )
    st.divider()
    nfo = Nfo(settings)
    st.header("Upload")
    if files := extract_files("display_mtcc_extract_files"):
        st.header("Nfo")
        with st.spinner(text="nfo creation..."):
            nfo.parse(files)
            upload_infos = get_upload_infos(files)
        st.success("nfo created")
        st.download_button(
            label="Download nfo",
            data=str(nfo),
            file_name=f"{nfo.filename}.nfo",
            mime="text/x-nfo",
            key="display_mtcc_download_nfo",
        )
        st.header("Torrent content")
        pres = Pres(settings, nfo.properties, upload_infos)
        with st.spinner(text="searching album..."):
            album = pres.search()
        if album:
            st.success(
                f"Album found {pres.properties.title} by {pres.properties.artist.name}"
            )
            display_torrent_contents(pres)
        else:
            st.error("Album not found")
            st.text("Try to find it with a research")
            if research := search_album("display_mtcc_search_album"):
                with st.spinner(text="Research album..."):
                    albums = pres.search(research)
                if albums:
                    st.success(f"{len(albums)} albums found")
                    album = display_album(albums)
                    if album:
                        pres.update_properties(album)
                        st.success(
                            f"Album Selected {album.title} by {album.artist.name}"
                        )
                        display_torrent_contents(pres)


def display_mtcc_pres(settings: dict) -> None:
    st.header("mtcc PRES")
    st.write(
        "###### mtcc PRES allows you to generate a torrent presentation by search by specifying the technical details yourself."
    )
    st.divider()
    pres = Pres(settings)
    technical_details, infos_download = extract_information()
    st.header("Find album")
    if research := search_album("display_mtcc_pres_search_album"):
        with st.spinner(text="Research album..."):
            albums = pres.search(research)
        if albums:
            st.success(f"{len(albums)} albums found")
            album = display_album(albums)
            if album:
                pres.nfo_properties.update(technical_details)
                pres.upload_infos.update(infos_download)
                pres.update_properties(album)
                st.success(f"Album selected {album.title} by {album.artist.name}")
                display_torrent_contents(pres)


def display_nfo_builder(settings: dict) -> None:
    st.header("mtcc Nfo Builder")
    st.write(
        "###### mtcc Nfo builder allows you to generate an .nfo from an uploaded album/single."
    )
    st.divider()
    nfo = Nfo(settings)
    st.header("Upload")
    if files := extract_files("display_nfo_builder"):
        st.header("Nfo")
        with st.spinner(text="nfo creation..."):
            nfo.parse(files)
        st.success("nfo created")
        st.download_button(
            label="Download nfo",
            data=str(nfo),
            file_name=f"{nfo.filename}.nfo",
            mime="text/x-nfo",
            key="display_nfo_builder_download_nfo",
        )
        st.code(str(nfo), language="text")


def main() -> None:
    display_header()
    settings = display_settings()
    mtcc, mtcc_pres, mtcc_nfo_builder = st.tabs(
        ["mtcc", "mtcc PRES", "mtcc Nfo Builder"]
    )
    with mtcc:
        display_mtcc(settings)
    with mtcc_pres:
        display_mtcc_pres(settings)
    with mtcc_nfo_builder:
        display_nfo_builder(settings)


if __name__ == "__main__":
    main()
