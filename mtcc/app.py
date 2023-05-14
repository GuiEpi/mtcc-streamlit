from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st
from nfo import Nfo
from pres import Pres
import utils


def display_header() -> None:
    st.title("Welcome to mtcc")
    st.text("Just upload your folder")


def display_uploader() -> UploadedFile:
    files = st.file_uploader(
        "Upload your file here.",
        accept_multiple_files=True,
        type=["wav", "mp3", "flac", "jpg", "jpeg", "png"],
    )

    if not (files):
        st.error("A file is needed.")

    return files


def extract_files():

    uploaded_files = display_uploader()

    if uploaded_files:
        return uploaded_files


def main() -> None:
    display_header()
    upload_infos = {}
    nb_file = 0
    total_size = 0
    nfo = Nfo()

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
        with st.spinner(text="searching album..."):
            nb_file = len(files)
            total_size = 0
            for file in files:
                total_size += file.size
            pres = Pres("", nfo.properties, upload_infos)
            pres.search()

        st.code(pres.torrent_name)
        st.code(str(pres), language="bbcode")


if __name__ == "__main__":
    main()
