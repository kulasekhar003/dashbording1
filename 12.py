#exp-12
import streamlit as st
import datetime

st.set_page_config(
    page_title = "New app" ,
    layout = "wide"
)
st.write("Name: B.Harini")
st.write("Reg. No: 211801370026")
email = st.text_input("Enter mail")
if not email:
    st.warning("Enter your email please")
    st.stop()
st.success("go ahead")

#forms
form = st.form("Basic form")
name = form.text_input("Name")
age = form.slider("Age" , min_value = 18 , max_value = 100 , step = 1)
date = form.date_input("Birthday" , value = datetime.date(2023 , 4 , 3))
submitted = form.form_submit_button("Submit")
if submitted:
    st.write(name , age , date)


st.write("hi")

def summ(a , b):
    return a + b

with st.echo():
    def mult(a , b):
        return a * b
    a = 10
    b = 20
    su = summ(a , b)
    mu = mult(a , b)
    st.write(su , mu)
st.write("This is outside")


st.help(datetime.time)