import streamlit as st
from PIL import Image
import cv2

st.write("Name: B.Harini")
st.write("Reg. No: 211801370026")
img = Image.open(r"C:\Users\HARSHINI\Pictures\Screenshots\Screenshot 2023-07-22 105656.png")
img = cv2.imread(r"C:\Users\HARSHINI\Pictures\Screenshots\Screenshot 2023-07-22 105706.png")
st.image(
    img ,
    caption = "Flower Image" ,
    width = 500 ,
    channels = "BGR"
)

st.audio(r"C:\Users\HARSHINI\Downloads\Closer.mp3" , start_time = 10)

st.video(r"C:\Users\HARSHINI\Downloads\Untitled video - Made with Clipchamp.mp4")

