import pandas as pd
import streamlit as st
import datetime
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('sleep.csv')
st.set_page_config(layout='wide')
st.markdown('<style>div.block-container</style>', unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Overview"

sidebar = st.sidebar

with sidebar:
    st.markdown('<center><h2>Sleep Health Data Analysis</h2></center>', unsafe_allow_html=True)

    if st.button('Overview', use_container_width=True):
        st.session_state.page = "Overview"

    if st.button('Dashboard', use_container_width=True):
        st.session_state.page = "Dashboard"


if st.session_state.page == "Overview":
    from pages import overview_page
    overview_page.render()


elif st.session_state.page == "Dashboard":
    st.title("📖 Dashboard")
    st.write("Intro to gsdgdfg course...")