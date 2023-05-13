from streamlit.runtime.uploaded_file_manager import UploadedFile
import streamlit as st
from nfo import Nfo


def display_header() -> None:
    st.title("Welcome to mtcc")
    st.text("Just upload your folder or copy and paste in the field below")


def display_widgets() -> UploadedFile:
    files = st.file_uploader(
        "Upload your file here.",
        accept_multiple_files=True,
        type=["wav", "mp3", "flac"],
    )

    if not (files):
        st.error("A file is needed.")

    return files


def extract_files():
    uploaded_files = display_widgets()

    if uploaded_files:
        return uploaded_files


def main() -> None:
    display_header()
    nfo = Nfo()

    if files := extract_files():
        with st.spinner(text="nfo creation..."):
            nfo.parse(files)
        st.success("nfo created")
        st.download_button(
            label="Download nfo",
            data=str(nfo),
            file_name=f"{nfo.filename}.nfo",
            mime="text/x-nfo",
        )


if __name__ == "__main__":
    main()
