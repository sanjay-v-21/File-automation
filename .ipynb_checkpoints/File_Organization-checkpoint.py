import streamlit as st
import os

def fileorganizer(path):
    extensions=[]
    files=os.listdir(path)

    for file in files:
        full_path=os.path.join(path,file)
        if os.path.isfile(full_path):
            ext=os.path.splitext(file)[1][1:]
            if ext not in extensions:
                extensions.append(ext)
    for ext in extensions:
        os.makedirs(os.path.join(path,ext),exist_ok=True)

    
    for file in files:
        full_path=os.path.join(path,file)
        if os.path.isfile(full_path):
            ext=os.path.splitext(file)[1][1:]
            if ext in extensions:
                dest=os.path.join(path,ext,file)
                os.rename(full_path,dest)
                
# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="File Organizer", layout="centered")

st.title("📁 File Organizer")
st.write("Organize files into folders based on file extensions")

path = st.text_input(
    "Enter folder path",
    placeholder="C:\\Users\\YourName\\Downloads"
)

if st.button("Organize Files"):
    if not path:
        st.error("Please enter a folder path")
    elif not os.path.exists(path):
        st.error("Invalid folder path")
    else:
        with st.spinner("Organizing files..."):
            fileorganizer(path)

        st.success("Files organized successfully!")

                