import streamlit as st

choice = st.sidebar.radio(
    label = "Choose the option" ,
    options = ("audio" , "video")
)
st.write("Name: B.Harini")
st.write("Reg. No: 211801370026")
if choice == "audio":
    st.audio(r"C:\Users\HARSHINI\Downloads\Closer.mp3")
    st.write("This is audio")
elif choice == "video":
    st.video(r"C:\Users\HARSHINI\Downloads\Untitled video - Made with Clipchamp.mp4")
    st.write("this is video")

col1 , col2 = st.columns([1 , 3] , gap = "small")
col1.audio(r"C:\Users\HARSHINI\Downloads\Closer.mp3")
col1.write("This is audio")
col2.video(r"C:\Users\HARSHINI\Downloads\Untitled video - Made with Clipchamp.mp4")

tab1 , tab2 = st.tabs(["audio" , "video"])
tab1.audio(r"C:\Users\HARSHINI\Downloads\Closer.mp3")
tab1.write("hi")
tab2.video(r"C:\Users\HARSHINI\Downloads\Untitled video - Made with Clipchamp.mp4")

exp = st.expander("See pic")
exp.write("Video and image")
exp.image(r"C:\Users\HARSHINI\Pictures\Screenshots\Screenshot 2023-07-22 105656.png" , width = 400)

st.write("One")
st.write("Two")
st.write("Three")

cont = st.container()
cont.write("One")
st.write("Two")
cont.write("Three")
st.write("This is last")
cont.write("Last")