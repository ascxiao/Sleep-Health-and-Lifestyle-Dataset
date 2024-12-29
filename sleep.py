import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats

# Load the data
sleep = pd.read_csv('sleep.csv')

sleep.columns = ['id', 'gender', 'age', 'occupation', 'duration', 'quality_level', 'physical_level', 'stress_level', 'bmi_category', 'bp', 'heart_rate', 'daily_steps', 'sleep_disorder']
sleep.plot(x = 'sleep_disorder', y = 'duration', kind = 'bar')
plt.show()