import streamlit as st
import pandas as pd
import numpy as np
import json

st.write("Name: B.Harini")
st.write("Reg. No: 211801370026")
#dataframe, tables, metric, json

df=pd.DataFrame(np.random.randn(4,10),columns=["cols"+str(i) for i in range(10)])
st.dataframe(df, width=300,height=240)
st.dataframe(np.random.randn(4,10))

st.table(df)

st.metric("TCS stock",value="3220.70",delta="19.10",delta_color="off")

f=open(r"C:\Users\HARSHINI\Desktop\Dash Board\images,videos,audios files\csvjson.json")
dt=json.load(f)
st.json(dt, expanded=False)
