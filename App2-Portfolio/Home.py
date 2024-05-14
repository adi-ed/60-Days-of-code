import streamlit as st
import pandas
import streamlit.components.v1 as components


st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/image.png")
    
with col2:
    st.title("Aditya Singh")
    content = "Hey there! My name is Aditya and i'm a budding Python developer and this static webpage is to showcase a list of Python Projects\
    developed as a consequence of that. There are 20 projects in the page made during throughout the course  \"Python Mega Course- Build 20 Apps in 60 days.\" You can contact me at adityasingh1416@gmail.com . The code and corresponding project files can be found at https://github.com/adi-ed/Py-60-days-20-Projects "
    st.info(content)
    
content = """
         Below you can find some of the apps built in Python. Feel free to contact me!
         """
st.write(content)


col3,  empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=';')
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        iframe_src = "www.github.com/adi_ed"
        components.iframe(iframe_src)
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])

