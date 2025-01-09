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

#Dropping blood pressure
sleep_transformed = sleep_transformed.drop(columns=['Blood Pressure (systolic/diastolic)'])

#Checking data types
print(sleep.info())
print(sleep_transformed.info())

#---------------------------------------

# Plotting the data

fig, axes = plt.subplots(1,2)

sns.set(style="ticks", rc={"lines.linewidth": 0.7})
sns.pointplot(x = 'Quality of Sleep (scale: 1-10)', y = 'Sleep Duration (hours)', data = sleep_transformed, hue = 'BMI Category', ci = 'sd', dodge = True, capsize = 0.1, ax= axes[0])

numerical_columns = sleep_transformed.select_dtypes(include=['number'])
sns.heatmap(numerical_columns.corr(), annot = True, fmt = ".2f", cmap = 'coolwarm', ax= axes[1])

sns.set(font_scale = 0.20)
plt.tight_layout()
plt.show()