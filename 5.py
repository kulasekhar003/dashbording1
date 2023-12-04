import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.header("Name: B.Harini")
st.header("Reg. No: 211801370026")
df = pd.DataFrame(np.random.randn(10 , 2) , 
                  columns = ["students" , "faculty"])
#line chart
st.subheader("Line Chart")
st.line_chart(df , y = ["students"])

st.subheader("Area Chart")
st.area_chart(df , y = ["faculty"])

st.subheader("Bar Chart")
st.bar_chart(df)

#matplotlib scatter
fig , ax = plt.subplots()
st.subheader("Scatter And Hist Chart")
ax.scatter(np.arange(10) , np.arange(10) ** 2)

ax.hist(np.random.randn(100) , bins = 10)
st.pyplot(fig)

st.subheader("Map")
places = pd.DataFrame({
        "lat" : [18.186891] ,
        "lon" : [83.398604]
    })
st.map(places)