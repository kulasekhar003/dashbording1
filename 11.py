#exp -11
import streamlit as st
import time

st.write("Name: B.Harini")
st.write("Reg. No: 211801370026")
txt = "% completed"
my_bar = st.progress(0 , text = txt)
for pr in range(100):
    time.sleep(0.1)
    my_bar.progress(pr + 1 , text = txt)

with st.spinner("wait for it..."):
    time.sleep(5)
st.write("wait over")

st.balloons()

st.snow()

e = RuntimeError("Exp")
st.exception(e)