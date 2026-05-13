## streamlit ko download krna pdega
import streamlit as st
from pathlib import Path
import os

st.title("📂 File Handling System")


menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Show Files",
        "Create File",
        "Read File",
        "Delete File",
        "Create Folder",
        "Delete Folder"
    ]
)


if menu == "Show Files":

    p = Path('')
    items = list(p.rglob('*'))

    st.subheader("Files & Folders")

    for index, file in enumerate(items):
        st.write(f"{index + 1} - {file}")


elif menu == "Create File":

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.warning("File already exists")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("File created successfully")


elif menu == "Read File":

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, 'r') as file:
                st.text(file.read())

        else:
            st.error("File not found")


elif menu == "Delete File":

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)
            st.success("File deleted")

        else:
            st.error("File not found")


elif menu == "Create Folder":

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.warning("Folder already exists")

        else:
            p.mkdir()
            st.success("Folder created")


elif menu == "Delete Folder":

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()
            st.success("Folder deleted")

        else:
            st.error("Folder not found")