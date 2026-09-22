import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("2022temprain.csv")

print(df.corr(numeric_only=True).round(2))

plt.title("상관 관계")

sns.heatmap(df.corr(numeric_only=True), annot = True)
plt.show()