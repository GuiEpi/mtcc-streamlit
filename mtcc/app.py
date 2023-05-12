import streamlit as st


def display_header() -> None:
    st.title("Welcome to mtcc")
    st.text("Just upload your folder or copy and paste in the field below")


def main() -> None:
    display_header()


if __name__ == "__main__":
    main()
