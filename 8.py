import streamlit as st
import datetime
from PIL import Image
import numpy as np
from io import StringIO

st.write("Name: B.Harshini")
st.write("Reg. No: 21180137002")
txt = st.text_area(
    label = "Write something" ,
    height = 50 ,
    max_chars = 50 ,
    placeholder = "Write here"
)
st.write(txt)

dat = st.date_input("Enter your birthday" ,
                    value = datetime.date(2023 , 4 , 11))
st.write(dat)

tim = st.time_input("Enter your meal time" , value = datetime.time(14 , 00))
st.write(tim)

fl = st.file_uploader(
    label = "Upload here"
)
if fl:
    st.write(fl.type)
    if "image" in fl.type:
        img = Image.open(fl)
        st.write(np.array(img).shape)
    elif fl.type == "text/plain":
        stringio = StringIO(fl.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

picture = st.camera_input("Take a pic")
if picture:
    img = Image.open(picture)
    st.write(np.array(img).shape)

color = st.color_picker("Pick a color")
if color:
    st.write("You selected" , color)