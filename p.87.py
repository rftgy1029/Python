import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import pandas as pd

from tkinter.tix import COLUMN

env = pd.read_csv('tomato_env.csv')
grow = pd.read_csv('tomato_grow.csv')

env = env.drop(columns=['내부 CO₂(ppm)', '지습(%)', '지온(도)'])

numerical_columns = env.select_dtypes(include=[float, int]).columns
print(numerical_columns)

plt.figure(figsize= (12,3))

for i in range(4):
    plt.subplot(1, 4, i+1)
    env.boxplot(column = numerical_columns[i])