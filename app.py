import pandas as pd
import streamlit as st
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('sleep.csv')
st.set_page_config(layout='wide')
st.markdown('<style>div.block-container</style>', unsafe_allow_html=True)
image = Image.open('Sleep_picture.jpg')

sidebar = st.sidebar

with sidebar:

    st.markdown('<center><h2>Sleep Health Data Analysis</h2></center>', unsafe_allow_html=True)

    if sidebar.button('Overview', use_container_width=True):
        st.session_state.page == "Overview"

    if sidebar.button('Dashboard', use_container_width=True):
        st.session_state.page == "Dashboard"

if st.session_state.page == "Overview":
    col1, col2 = st.columns([0.5, 0.5]);
    
    with col1:
        st.image(image, width=500)
    with col2:
        st.markdown


if st.session_state.page == "Dashboard":
    st.title("📖 Dashboard")
    st.write("Intro to gsdgdfg course...")