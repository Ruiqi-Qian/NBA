import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import legend

df_per_ts = pd.read_csv("E:/Advanced program/PER-TS%.csv")
print(df_per_ts.head())

#PER BOXPLOT
plt.figure(figsize = (10,6))
sns.boxplot(y=df_per_ts['PER'],x=df_per_ts['Season'])
plt.grid(True)
plt.show()

df_19= pd.read_csv("E:/Advanced program/merged_data_pos-2019.csv")
df_20= pd.read_csv("E:/Advanced program/merged_data_pos-2020.csv")
df_21 = pd.read_csv("E:/Advanced program/merged_data_pos-2021.csv")
df_22 = pd.read_csv("E:/Advanced program/merged_data_pos-2022.csv")

df_19['season'] = "2019-20"
df_20['season'] = "2020-21"
df_21['season'] = "2021-22"
df_22['season'] = "2022-23"

#PTS,SEASON,Density plot
df_all_seasons = pd.concat([df_19[['pts','season']], df_20[['pts','season']], df_21[['pts','season']], df_22[['pts','season']]], ignore_index=True)
print(df_all_seasons)
plt.figure(figsize=(10,6))
sns.kdeplot(data=df_all_seasons,x='pts',hue='season',fill=True,common_norm=False,alpha=0.4)
plt.xlabel("Average points per game (PTS)",fontsize=12)
plt.ylabel("Density",fontsize=12)
plt.legend(title='season')
plt.grid(True)
plt.show()

#2019-20 PTS and salary's scatter plot and regression curve
plt.figure(figsize=(10,6))
sns.regplot(data=df_19,x='season.y',y='pts',scatter_kws={'alpha':0.5}, line_kws={"color":"red"})
plt.xscale("log")
plt.xlabel("Salary")
plt.ylabel("Average points per game")
plt.title("2019-20 season Player Salary vs. Points per game")
plt.legend()
plt.grid(True)
plt.show()

#2020-21 pts and salary's scatter plot
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_20,x='2020/21',y='pts',alpha=0.4,edgecolor='k')
plt.xlabel("Salary")
plt.ylabel("Average points per game")
plt.title("2020-21 season Player Salary vs. Points per game")
plt.legend()
plt.grid(True)
plt.show()

#2021-22 pts and salary's scatter plot
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_21,x='2021/22',y='pts',alpha=0.4,edgecolor='k')
plt.xlabel("Salary")
plt.ylabel("Average points per game")
plt.title("2021-22 season Player Salary vs. Points per game")
plt.legend()
plt.grid(True)
plt.show()

#2022-23 pts and salary's scatter plot
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_22,x='2022/23',y='pts',alpha=0.4,edgecolor='k')
plt.xlabel("Salary")
plt.ylabel("Average points per game")
plt.title("2022-23 season Player Salary vs. Points per game")
plt.legend()
plt.grid(True)
plt.show()

#2022-23 correlation heatmaps
select_columns = ["pts","reb","ast","2022/23"]
df_selectd_22 = df_22[select_columns]
corr_matrix_22 = df_selectd_22.corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix_22,annot=True,cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.legend(title="Correlation Heatmap: Points, Rebounds, Assists vs Salary")
plt.show()

#2021-22 correlation heatmaps
df_selectd_21 = df_21[['pts','reb','ast','2021/22']]
corr_matrix_21 = df_selectd_21.corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix_21,annot=True,cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.legend(title="Correlation Heatmap: Points, Rebounds, Assists vs Salary")
plt.show()

#2020-21 correlation heatmaps
df_selectd_20 = df_20[['pts','reb','ast','2020/21']]
corr_matrix_20 = df_selectd_20.corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix_20,annot=True,cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.legend(title="Correlation Heatmap: Points, Rebounds, Assists vs Salary")
plt.show()

#2019-20 correlation heatmaps
df_selectd_19 = df_19[['pts','reb','ast','season.y']]
corr_matrix_19 = df_selectd_19.corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix_19,annot=True,cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.legend(title="Correlation Heatmap: Points, Rebounds, Assists vs Salary")
plt.show()

#2019
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
sns.boxplot(data=df_19,x="Pos",y="pts",palette="Blues")
plt.title("19-20 season Position vs. Points per Game")

plt.subplot(1,3,2)
sns.boxplot(data=df_19,x="Pos",y="reb",palette="Greens")
plt.title("19-20 season Position vs. Rebound per Game")

plt.subplot(1,3,3)
sns.boxplot(data=df_19,x="Pos",y="ast",palette="Reds")
plt.title("19-20 season Position vs. Ast per Game")

plt.tight_layout()
plt.show()

#2020
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
sns.boxplot(data=df_20,x="Pos",y="pts",palette="Blues")
plt.title("20-21 season Position vs. Points per Game")

plt.subplot(1,3,2)
sns.boxplot(data=df_20,x="Pos",y="reb",palette="Greens")
plt.title("20-21 season Position vs. Rebound per Game")

plt.subplot(1,3,3)
sns.boxplot(data=df_20,x="Pos",y="ast",palette="Reds")
plt.title("20-21 season Position vs. Ast per Game")

plt.tight_layout()
plt.show()

#2021
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
sns.boxplot(data=df_21,x="Pos",y="pts",palette="Blues")
plt.title("21-22 season Position vs. Points per Game")

plt.subplot(1,3,2)
sns.boxplot(data=df_21,x="Pos",y="reb",palette="Greens")
plt.title("21-22 season Position vs. Rebound per Game")

plt.subplot(1,3,3)
sns.boxplot(data=df_21,x="Pos",y="ast",palette="Reds")
plt.title("21-22 season Position vs. Ast per Game")

plt.tight_layout()
plt.show()

#2022
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
sns.boxplot(data=df_22,x="Pos",y="pts",palette="Blues")
plt.title("22-23 season Position vs. Points per Game")

plt.subplot(1,3,2)
sns.boxplot(data=df_22,x="Pos",y="reb",palette="Greens")
plt.title("22-23 season Position vs. Rebound per Game")

plt.subplot(1,3,3)
sns.boxplot(data=df_22,x="Pos",y="ast",palette="Reds")
plt.title("22-23 season Position vs. Ast per Game")

plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df_19, x="Pos", y="season.y", palette="coolwarm")
plt.title("19-20 season Average Salary by Position")
plt.ylabel("Average Salary")
plt.xlabel("Position")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df_20, x="Pos", y="2020/21", palette="coolwarm")
plt.title("20-21 season Average Salary by Position")
plt.ylabel("Average Salary")
plt.xlabel("Position")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df_21, x="Pos", y="2021/22", palette="coolwarm")
plt.title("21-22 season Average Salary by Position")
plt.ylabel("Average Salary")
plt.xlabel("Position")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(data=df_22, x="Pos", y="2022/23", palette="coolwarm")
plt.title("22-23 season Average Salary by Position")
plt.ylabel("Average Salary")
plt.xlabel("Position")
plt.grid(True)
plt.show()