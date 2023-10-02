import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col, col2 = st.columns(2)
with col:
    st.image("Images/ph.jpg", width=600)

with col2:
    st.write("Pawan Kumar")
    content = """
    Hi, I am Pawan! I am an student of Symbiosis Institute Of Computer Studies And Research. Currently I am pursuing BCA 
    from there. I am a founder of GUI based web app name MY Todo App. I am a software developer also and doing part
    time job through freelancing.
    """
    st.info(content)
content2 = "Below you can find some of the apps I have built in python. Feel free to contact me!"
st.write(content2)

col3, empty_col,  col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep=";")
with col3:
    a=1
    if(a<=10):
        for index, row in df[:10].iterrows():
            st.header(row['title'])
            st.write(row['description'])
            st.image(f"Images/{a}.png")
            st.write(f"[Source code]({row['url']})")
            a+=1

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("Images/"+row['image'])
        st.write(f"[Source code]({row['url']})")