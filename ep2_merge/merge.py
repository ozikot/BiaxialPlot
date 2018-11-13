import pandas as pd
import matplotlib.pyplot as plt

# 心拍と体表温度のCSVファイルを読み込む
df_hb = pd.read_csv('..//csv_file//heartbeat.csv')
df_tm = pd.read_csv('..//temp_bs_edited.csv')

print(df_tm.head())