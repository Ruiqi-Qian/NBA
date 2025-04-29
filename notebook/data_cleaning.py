import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("E:/Advanced program/NBA Advanced Stats(2019 - 2024).csv")
print(f"Loaded NBA Advanced Stats with {df.shape[0]} rows.")

print("First 5 rows of the NBA Advanced Stats dataset:")
print(df.head())

print("\nDataset Info")
print(df.info())

print("\nSummary Statictics")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nColumn names:")
print(df.columns)

df_per_ts = df[['Season','Player','PER','TS%']].dropna()
save_path_PER = "E:/Advanced program/PER-TS%.csv"
df_per_ts.to_csv(save_path_PER,index=False)
print(df_per_ts)

df_salary = pd.read_csv("E:/Advanced program/NBA Salaries(2019-2024).csv")
print(df_salary.head())

df_2019_20 = df_salary[['playerName','2019/20']].dropna()
df_2020_21 = df_salary[['playerName','2020/21']].dropna()
df_2021_22 = df_salary[['playerName','2021/22']].dropna()
df_2022_23 = df_salary[['playerName','2022/23']].dropna()
df_2023_24 = df_salary[['playerName','2023/24']].dropna()
df_2019_20.rename(columns={'playerName':'Player_name'}, inplace=True)
df_2020_21.rename(columns={'playerName':'Player_name'}, inplace=True)
df_2021_22.rename(columns={'playerName':'Player_name'}, inplace=True)
df_2022_23.rename(columns={'playerName':'Player_name'}, inplace=True)
df_2023_24.rename(columns={'playerName':'Player_name'}, inplace=True)

df_selectd = df[['Season','Player','Pos']]
df_selectd.rename(columns={'Player':'player_name','Season':'season'}, inplace=True)
save_path_6 = "E:/Advanced program/player_pos.csv"
df_selectd.to_csv(save_path_6, index=False)

df_pos = pd.read_csv("E:/Advanced program/player_pos.csv")

seasons = df_pos["season"].unique()

for season in seasons:
    df_season = df_pos[df_pos["season"] == season]
    file_name = f"season_{season}.csv"
    save_path_7 = f"E:/Advanced program/{file_name}"
    df_season.to_csv(save_path_7, index=False)

df_pos_2019 = pd.read_csv("E:/Advanced program/season_2019.csv")
df_pos_2020 = pd.read_csv("E:/Advanced program/season_2020.csv")
df_pos_2021 = pd.read_csv("E:/Advanced program/season_2021.csv")
df_pos_2022 = pd.read_csv("E:/Advanced program/season_2022.csv")

df_merged_data_2019 = pd.read_csv("E:/Advanced program/merged_data_19-20.csv")
df_merged_data_2020 = pd.read_csv("E:/Advanced program/merged_data_20-21.csv")
df_merged_data_2021 = pd.read_csv("E:/Advanced program/merged_data_21-22.csv")
df_merged_data_2022 = pd.read_csv("E:/Advanced program/merged_data_22-23.csv")

df_merged_data_pos_2019 = pd.merge(df_merged_data_2019, df_pos_2019, on='player_name', how='left').dropna(subset=['Pos'])
df_merged_data_pos_2020 = pd.merge(df_merged_data_2020, df_pos_2020, on='player_name', how='left').dropna(subset=['Pos'])
df_merged_data_pos_2021 = pd.merge(df_merged_data_2021, df_pos_2021, on='player_name', how='left').dropna(subset=['Pos'])
df_merged_data_pos_2022 = pd.merge(df_merged_data_2022, df_pos_2022, on='player_name', how='left').dropna(subset=['Pos'])

save_path_8 = "E:/Advanced program/merged_data_pos-2019.csv"
save_path_9 = "E:/Advanced program/merged_data_pos-2020.csv"
save_path_10 = "E:/Advanced program/merged_data_pos-2021.csv"
save_path_11 = "E:/Advanced program/merged_data_pos-2022.csv"
df_merged_data_pos_2019.to_csv(save_path_8, index=False)
df_merged_data_pos_2020.to_csv(save_path_9, index=False)
df_merged_data_pos_2021.to_csv(save_path_10, index=False)
df_merged_data_pos_2022.to_csv(save_path_11, index=False)