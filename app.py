import pandas as pd
import streamlit as st
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('sleep.csv')
st.set_page_config(layout='wide')
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)