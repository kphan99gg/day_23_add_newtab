import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

data = pd.read_csv("data.csv", sep=';')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Ardit Sulce")
    content = '''
    Hi, I am Ardit! I am a python programmer, teacher, and founder of PythonHow.
    '''
    st.info(content)

content = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.subheader(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    for index, row in data[:10].iterrows():
        st.title(row['title'])
        st.info(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.title(row['title'])
        st.info(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")
