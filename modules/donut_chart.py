import streamlit as st
import plotly.graph_objects as go
from modules import dataset as data

def gender():
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

def occupation():
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

def bmi():
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

def sleep_disorder():
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