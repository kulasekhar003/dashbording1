import streamlit as st
import pandas as pd
import numpy as np
import time

st.header("Name: B.Harini")
st.header("Reg. No: 211801370026")
pr = st.button("Time is:")
if pr == True:
    st.write(time.time())

def fn():
     st.write(time.time())

st.button("Time" , on_click = fn)

#Download csv file
df = pd.DataFrame(
    np.random.randn(10 , 2) ,
    columns = ["col1" , "col2"]
)
data = df.to_csv().encode("utf-8")

st.download_button(
    label = "Download this" ,
    data = data ,
    file_name = r"C:\Users\HARSHINI\Downloads\All India.csv",
    mime = "text/csv"
)

#Download text file
text_contents = "This is some text"
st.download_button("Please download" , text_contents)

#Download image file
file = open(r"C:\Users\HARSHINI\Pictures\Screenshots\Screenshot 2023-06-09 103611.png" , "rb")
btn = st.download_button(
    label = "Download the image" ,
    data = file ,
    file_name = "Screenshot 2023-06-09 103611.png" ,
    mime = "Screenshot 2023-06-09 103611.png"
)

#checkbox
ck = st.checkbox("I agree" , value = False)
if ck:
    st.write("Agreement reached")

#radio button
food = st.radio("Select your class?" ,
                ("Class1" , "Class2" , "Class3"))
if food == "Class1":
    st.write("You are in Class1")
elif food == "Class2":
    st.write("You are in Class2")
elif food == "Class3":
    st.write("You are in Class3")

#selectbox
option = st.selectbox("Where do you live?" ,
                      ("vizag" , "vzm" , "hostel"))
if option == "vizag":
    st.write("You are in Vizag")
elif option == "vzm":
    st.write("You are in Vizianagaram")
elif option == "hostel":
    st.write("You are in Hostel")