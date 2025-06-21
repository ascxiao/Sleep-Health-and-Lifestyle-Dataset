import streamlit as st
import datetime

def render():
    sidebar = st.sidebar

    with sidebar:
        box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
        st.write(f"Last updated by: \n {box_date}")