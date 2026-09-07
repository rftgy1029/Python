import koreanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("2022temprain.csv")

print(df.head())

# 1. 시본으로 페어플롯 생성
sns.pairplot(df)

# 2. 화면에 실제 그래프 창을 띄우는 핵심 명령어!
plt.show()