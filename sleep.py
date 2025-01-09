import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats

# Load the data
sleep = pd.read_csv('sleep.csv')

sleep_transformed = sleep.copy()

# Transform the data
sleep_transformed['Person ID'] = sleep_transformed['Person ID'].astype('int16')
sleep_transformed['Gender'] = sleep_transformed['Gender'].astype('category')
sleep_transformed['Age'] = sleep_transformed['Age'].astype('int16')
sleep_transformed['Occupation'] = sleep_transformed['Occupation'].astype('category')
sleep_transformed['Sleep Duration (hours)'] = sleep_transformed['Sleep Duration (hours)'].astype('float32')
sleep_transformed['Physical Activity Level (minutes/day)'] = sleep_transformed['Physical Activity Level (minutes/day)'].astype('int16')
sleep_transformed['Stress Level (scale: 1-10)'] = sleep_transformed['Stress Level (scale: 1-10)'].astype('category')
sleep_transformed['BMI Category'] = sleep_transformed['BMI Category'].astype('category')
sleep_transformed['Heart Rate (bpm)'] = sleep_transformed['Heart Rate (bpm)'].astype('int16')
sleep_transformed['Daily Steps'] = sleep_transformed['Daily Steps'].astype('int16')
sleep_transformed['Sleep Disorder'] = sleep_transformed['Sleep Disorder'].astype('category')

#Round up quality of sleep > int > category
sleep_transformed['Quality of Sleep (scale: 1-10)'] = sleep_transformed['Quality of Sleep (scale: 1-10)'].apply(lambda x: np.ceil(x)).astype('int16').astype('category')

# Reorder the categories
sleep_transformed['Quality of Sleep (scale: 1-10)'] = sleep_transformed['Quality of Sleep (scale: 1-10)'].cat.set_categories(new_categories = [1,2,3,4,5,6,7,8,9,10], ordered = True)
sleep_transformed['Stress Level (scale: 1-10)'] = sleep_transformed['Stress Level (scale: 1-10)'].cat.set_categories(new_categories = [1,2,3,4,5,6,7,8,9,10], ordered = True)
sleep_transformed['BMI Category'] = sleep_transformed['BMI Category'].cat.set_categories(new_categories = ['Underweight', 'Normal', 'Overweight', 'Obese'], ordered = True)

print(sleep.info())
print(sleep_transformed.info())
