import streamlit as st
from PIL import Image
import pandas as pd

def render():
    image = Image.open('Sleep_picture.jpg')
    def go_dashboard():
        st.session_state.page = "Dashboard"

    st.markdown('<center><h1>Sleep Health and Lifestyle</h2></center>', unsafe_allow_html=True)

    col1, col2 = st.columns([0.5, 0.5], gap = 'large')

    with col1:
        st.image(image, use_container_width=True)
    with col2:
        st.markdown('<left><h2>The Problem</h2></left>', unsafe_allow_html=True)
        st.markdown("<p>Living in today's fast-paced world, sleep has become an overlooked components of our health. \
                    Poor sleep habits, rising stress levels, and sedantary routines and increasinly linked to various \
                    chronic health problems, however the roots of these sleep habits and disorders remained complex and \
                    multidimensional. With this, organization and healthcare providers may need data-driven insights to \
                    understand different aspects that contribute to poor sleep, how it differentiates between different \
                    demographics, and what interventions are possible that might improve health outcomes.\
                    <i><b>How can we identify and address the key factors influencing poor sleep quality and \
                    sleep disorders across different demographics to support healthier living?</b></i></p>", unsafe_allow_html=True)

    dataset = pd.DataFrame({
        "Variable Category": ['Demographics', 'Sleep Metrics', 'Health Inidcators', 'Lifestyle Factors'],
        "Variables" : ['Person ID, Age, Gender, Occupation', 'Sleep Duration, Quality of Sleep (1-10), Sleep Disorder', 'BMI Category, Blood Pressure, Heart Rate (bpm)', 'Physical Activity (minutes/day), Stress Level (scale 1-10), Daily Steps']
    })
    dataset2 = pd.DataFrame({
        "Variable": ['Person ID', 'Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep (1-10)', 'Sleep Disorder', 'BMI Category', 'Heart Rate bpm', 'Physical Activity (minutes/day)', 'Stress level (scale1-10)', 'Daily Steps'],
        "Data Type" : ['index', 'category', 'int16', 'category', 'float32', 'float64', 'category', 'category', 'int16', 'int16', 'int64', 'int16']
    })

    col3, col4 = st.columns([0.5, 0.5])
    with col3:
        st.markdown('<center><h2>Dataset Overview</h2></center>', unsafe_allow_html=True)
        st.table(dataset)
    with col4:
        st.markdown('<center><h2>Variable Description</h2></center>', unsafe_allow_html=True)
        st.table(dataset2)

    st.button('Go to Dashboard', use_container_width=True, on_click=go_dashboard)