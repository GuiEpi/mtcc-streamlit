from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st
from nfo import Nfo
from pres import Pres
import config
import utils


def display_header() -> None:
    st.title("Welcome to mtcc")
    st.text("mtcc is a content creator to upload music torrent")


def display_sidebar() -> dict:
    options = (banner for banner in config.PRES_BANNERS)

    with st.sidebar:
        st.title("Settings")
        ripper = st.text_input("Ripper", config.NFO_RIPPER)
        uploader = st.text_input("Uploader", config.NFO_UPLOADER)
        selected_banner = st.sidebar.selectbox("Choose your banner theme", options)
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


def display_uploader() -> UploadedFile:
    files = st.file_uploader(
        "Upload your file here.",
        accept_multiple_files=True,
        type=["wav", "mp3", "flac", "jpg", "jpeg", "png"],
    )

    if not (files):
        st.error("A file is needed.")

    return files


def extract_files() -> UploadedFile:

    uploaded_files = display_uploader()

    if uploaded_files:
        return uploaded_files


def main() -> None:
    display_header()
    settings = display_sidebar()
    upload_infos = {}
    nb_file = 0
    total_size = 0
    nfo = Nfo(settings)

    st.header("Nfo")
    if files := extract_files():
        with st.spinner(text="nfo creation..."):
            nb_file = len(files)
            total_size = 0
            for file in files:
                total_size += file.size

            upload_infos["nb_files"] = nb_file
            upload_infos["total_size"] = utils.convert_size(total_size)
            nfo.parse(files)
        st.success("nfo created")
        st.download_button(
            label="Download nfo",
            data=str(nfo),
            file_name=f"{nfo.filename}.nfo",
            mime="text/x-nfo",
        )
        st.header("Torrent content")
        with st.spinner(text="searching album..."):
            nb_file = len(files)
            total_size = 0
            for file in files:
                total_size += file.size
            pres = Pres(settings, "", nfo.properties, upload_infos)
            pres.search()
        st.success(f"Album found {pres.properties.title} by {pres.properties.artist.name}")
        st.text("Torrent name")
        st.code(pres.torrent_name)
        st.text("Torrent description")
        st.code(str(pres), language="bbcode")


if __name__ == "__main__":
    main()
