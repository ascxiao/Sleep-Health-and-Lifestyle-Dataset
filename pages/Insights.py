import streamlit as st
from PIL import Image
import pandas as pd
from modules import sidebar

df = pd.read_csv('sleep.csv')
st.set_page_config(layout='wide')
st.markdown('<style>div.block-container</style>', unsafe_allow_html=True)

sidebar.render()

image = Image.open('Sleep_picture.jpg')
def go_dashboard():
    st.session_state.page = "Dashboard"

st.markdown('<center><h1>Insights</h2></center>', unsafe_allow_html=True)

summary = pd.DataFrame({
    "Analytical Question": ['Which factors are most associated with low sleep quality?',
                             'How do sleep disorders vary by age, gender, and occupation?',
                             'Is there a link between physical activity, stress levels, and sleep duration?',
                             'Do individuals with better cardiovascular indicators (e.g. lower heart rate, normal blood pressure) sleep better?',
                             'What lifestyle patterns distinguish individuals without sleep disorders from those with insomnia or apnea?'],
    "Insights" : ['Top factors associated with sleep quality include Daily Steps, Physical Activity Level, and Age, contributing up to 25–27% in the Random Forest model. While no factor shows a strong individual correlation, these three stand out in relative importance based on the regression analysis',
                   'Sleep disorders vary across demographics. Insomnia is more common in males, while females are more affected by Sleep Apnea. The 36–45 age group shows the highest occurrence of both disorders, while no cases of Sleep Apnea were found in participants over 66. Office workers are most affected by both conditions, followed by students with Insomnia. Overall, Insomnia is more prevalent across all groups. This suggests that individuals engaged in work or academics—particularly males in their 30s–40s—may be more prone to sleep disorders due to environmental stress',
                    'No significant relationships were found between Physical Activity Level, Stress Level, and Sleep Duration. Correlation values were all near zero (e.g., -0.002, 0.054), and regression plots showed flat trends, indicating minimal or no linear association between these factors.',
                      'No significant relationship was found between cardiovascular factors and sleep duration. Sleep duration is evenly distributed across blood pressure categories, with hypothesis testing (p = 0.233) supporting this. However, participants with low heart rates appear less prone to sleep disorders, while most with disorders have normal heart rates.',
                      'Sleep Apnea is linked to a higher median stress level, while Insomnia is more common among those with higher physical activity. Both disorders show similar distributions in daily steps and overall spread. However, Mann-Whitney tests indicate no significant difference between the two disorders across these factors.']
}).reset_index(drop=True)

summary.index = summary.index + 1

st.table(summary)
st.markdown("[📓 View Full Analysis Notebook](https://github.com/ascxiao/Sleep-Health-and-Lifestyle-Dataset/blob/main/sleep.ipynb)")
