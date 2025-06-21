import streamlit as st
from pages import About
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
from modules import dataset, processing as prc, donut_chart as dc
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
        dc.gender()

    if donut == 'Occupation':
        dc.occupation()

    if donut == 'BMI Category':
        dc.bmi()

    if donut == 'Sleep Disorder':
        dc.sleep_disorder()
st.divider()

col4, col5 = st.columns([0.4, 0.6])

with col4:
    avg_sleep = df.groupby('Gender')['Quality of Sleep (scale: 1-10)'].mean().reset_index()
    fig = px.bar(avg_sleep, x = 'Gender', y ='Quality of Sleep (scale: 1-10)',
                 title = "Sleep Quality by Gender", hover_data = ['Quality of Sleep (scale: 1-10)'],
                template = 'gridon', height = 500, color = 'Gender')
    st.plotly_chart(fig, use_container_width=True)

with col5:
    fig = px.box(df, x='Age Group', y = 'Sleep Duration (hours)',
                 title = 'Sleep Duration by Age Group', hover_data=['Sleep Duration (hours)'],
                 template = 'gridon', height = 500, color = 'Age Group')
    st.plotly_chart(fig, use_container_width=True)

st.divider()

col6, col7= st.columns([0.8, 0.2], border=True)

with col6:
    values = st.slider('No. of Previews', 0, 20, 5)
    global importance
    importance = prc.importance(values)

    fig = px.bar(importance, x = importance.values, y = importance.index, orientation='h',
                 title = 'Depictors of Sleep Quality', template='gridon', height=500)
    fig.update_layout(yaxis=dict(autorange='reversed'))
    st.plotly_chart(fig, use_container_width=True)

with col7:
    st.markdown('<center><h4>Top 5 Indicators of Sleep Quality</h4><center>', unsafe_allow_html=True)
    st.divider()

    st.write(f"1. {importance.index[0]}")
    st.write(f"2. {importance.index[1]}")
    st.write(f"3. {importance.index[2]}")
    st.write(f"4. {importance.index[3]}")
    st.write(f"5. {importance.index[4]}")
st.divider()

