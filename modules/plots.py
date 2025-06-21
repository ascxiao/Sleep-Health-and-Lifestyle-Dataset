import streamlit as st
import plotly.graph_objects as go
from modules import dataset as data
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

def regplot(x, y, reg = False):
    fig = px.scatter(data.sleep_transformed, x= x, y = y, title =f'{x} vs {y}', template = 'gridon')

    if reg:
        X = data.sleep_transformed[[x]]
        y = data.sleep_transformed[y]

        model = LinearRegression().fit(X, y)
        x_range = np.linspace(X.min(), X.max(), 100)
        y_pred = model.predict(x_range)

        fig.add_traces(go.Scatter(
            x=x_range.flatten(),
            y=y_pred,
            mode="lines",
            name="Regression Line",
            line=dict(color="red", dash="dash")
        ))
    st.plotly_chart(fig, use_container_width=True)

def barplot(x):

    value_counts = data.sleep_transformed.groupby([x, 'Sleep Disorder']).size().reset_index()
    value_counts.columns=[x, 'Sleep Disorder','Count']

    fig = px.bar(value_counts, x= x, y = 'Count', color = 'Sleep Disorder',title =f'Count of {x} with Sleep Disorders', template = 'gridon', barmode = 'group')

    st.plotly_chart(fig, use_container_width=True)