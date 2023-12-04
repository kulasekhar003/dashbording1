import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header("Name: B. Harini")
st.header("Reg. No: 211801370026")
st.text("Hello.")

st.write("How are you")

#df=pd.read_csv(r"C:\Users\HARSHINI\Downloads\All India.csv")
#df

dc={"a" : 10, "b" : 20, "c" : 30}

fig,ax=plt.subplots()
ax.scatter(np.arange(5),np.arange(5)**2)

st.title("This is the title")
st.header("This is header section")
st.subheader("This is sub header section")

code='''def func():
    print(np.arange(10))
'''
st.code(code,language="python")
