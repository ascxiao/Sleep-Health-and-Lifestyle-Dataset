#Importing packages and loading the dataset

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats

# Load the data
sleep = pd.read_csv('sleep.csv')
sleep.set_index('Person ID', inplace=True)

sleep_transformed = sleep.copy()

# Transform the data
sleep_transformed['Gender'] = sleep_transformed['Gender'].astype('category')
sleep_transformed['Age'] = sleep_transformed['Age'].astype('int16')
sleep_transformed['Occupation'] = sleep_transformed['Occupation'].astype('category')
sleep_transformed['Sleep Duration (hours)'] = sleep_transformed['Sleep Duration (hours)'].astype('float32')
sleep_transformed['Physical Activity Level (minutes/day)'] = sleep_transformed['Physical Activity Level (minutes/day)'].astype('int16')
sleep_transformed['BMI Category'] = sleep_transformed['BMI Category'].astype('category')
sleep_transformed['Heart Rate (bpm)'] = sleep_transformed['Heart Rate (bpm)'].astype('int16')
sleep_transformed['Daily Steps'] = sleep_transformed['Daily Steps'].astype('int16')
sleep_transformed['Sleep Disorder'] = sleep_transformed['Sleep Disorder'].astype('category')

# Reorder the categories
sleep_transformed['BMI Category'] = sleep_transformed['BMI Category'].cat.set_categories(new_categories = ['Underweight', 'Normal', 'Overweight', 'Obese'], ordered = True)

avg_sleep = np.round(sleep_transformed['Sleep Duration (hours)'].mean(),2)
avg_stress = np.round(sleep_transformed['Stress Level (scale: 1-10)'].mean(),2)
avg_physical = np.round(sleep_transformed['Physical Activity Level (minutes/day)'].mean(),2)
percent_disorders = np.round((sleep_transformed['Sleep Disorder'].count()) / (len(sleep_transformed['Sleep Disorder'])) * 100, 2)
percent_gender = np.round(((sleep_transformed['Gender'].value_counts()['Male'])) / (len(sleep_transformed['Gender'])) * 100, 2)

percent_occupation = sleep_transformed['Occupation'].value_counts(normalize=True)
percent_bmi = sleep_transformed['BMI Category'].value_counts(normalize=True)


