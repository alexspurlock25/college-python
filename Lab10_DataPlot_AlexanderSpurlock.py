# Alexander Spurlock
# Nov 16th, 2022
# Lab 10 - Data Plot

import matplotlib.pyplot as mplot
import pandas as pd

df = pd.read_csv('insurance.csv')

print(df)

df.plot(kind='scatter', x='bmi', y='charges')