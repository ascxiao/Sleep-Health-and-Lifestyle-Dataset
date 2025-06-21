import streamlit as st
from pages import About
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
from modules import dataset
import numpy as np

st.set_page_config(layout='wide')

sidebar = st.sidebar

with sidebar:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by: \n {box_date}")

df=dataset.sleep_transformed
data = dataset

st.markdown('<style>div.block-container</style>', unsafe_allow_html=True)

st.markdown('<center><h1>Sleep Health and Lifestyle Analysis Dashboard</h1></center>', unsafe_allow_html=True)

col1, col2, col3= st.columns([0.15, 0.65, 0.20], border=True)

with col1:
    st.metric('Participant Count', len(df))
    st.metric('Avg Sleep Duration', f"{data.avg_sleep:.2f} hrs")
    st.metric('Avg Stress Level', f"{data.avg_stress:.2f}")
    st.metric('Avg Physical Activity Level', f"{data.avg_physical:.2f}")
    st.metric('Percentage with Sleep Disorders', f"{data.percent_disorders:.2f} %") 

with col3:
    donut = st.radio('Choose variable',
                     ['Gender',
                     'Occupation',
                     'BMI Category',
                     'Sleep Disorder'])
    
with col2:
    if donut == 'Gender':
        labels = ['Male', 'Female']
        values = [data.percent_gender, 100 - data.percent_disorders]

        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # 0.0 = pie, 0.5 = donut
        marker=dict(colors=["#F53621", "#A64338"])
        )])

        fig.update_layout(
            title_text="Distribution of Participants' Gender",
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)  

    if donut == 'Occupation':
        labels = [data.percent_occupation.index.tolist()[0], data.percent_occupation.index.tolist()[1], data.percent_occupation.index.tolist()[2], data.percent_occupation.index.tolist()[3]]
        values = [data.percent_occupation.values.tolist()[0],data.percent_occupation.values.tolist()[1], data.percent_occupation.values.tolist()[2], data.percent_occupation.values.tolist()[3]]

        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # 0.0 = pie, 0.5 = donut
        marker=dict(colors=["#E6A7A7", "#CC4A3E", "#DA4C7E", "#C623A5"])
        )])

        fig.update_layout(
            title_text="Distribution of Participants' Occupation",
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)  

    if donut == 'BMI Category':
        labels = [data.percent_bmi.index.tolist()[0], data.percent_bmi.index.tolist()[1], data.percent_bmi.index.tolist()[2], data.percent_bmi.index.tolist()[3]]
        values = [data.percent_bmi.values.tolist()[0],data.percent_bmi.values.tolist()[1], data.percent_bmi.values.tolist()[2], data.percent_bmi.values.tolist()[3]]

        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # 0.0 = pie, 0.5 = donut
        marker=dict(colors=["#E1A7E6", "#B43ECC", "#984CDA", "#4123C6"])
        )])

        fig.update_layout(
            title_text="Distribution of Participants' BMI Category",
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)  


    if donut == 'Sleep Disorder':
        labels = ['With Sleep Disorder', 'Without Sleep Disorder']
        values = [data.percent_disorders, (100 - data.percent_disorders)]

        fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # 0.0 = pie, 0.5 = donut
        marker=dict(colors=["#E68014", "#F9BDAD"])
        )])

        fig.update_layout(
            title_text='Distribution of Sleep Disorder Cases',
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)
st.divider()
      