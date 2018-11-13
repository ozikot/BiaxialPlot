import pandas as pd

def main():
    # 心拍と体表温度のCSVファイルを読み込む
    df_hb = pd.read_csv('..//csv_file//heartbeat.csv')
    df_tm = pd.read_csv('..//csv_file//temp_bs_edited.csv')

    # 二つのデータをマージ
    df_me = pd.merge(df_hb, df_tm)

    # CSVファイルに書き込み
    df_me.to_csv('..//csv_file//merged.csv', index=False)

if __name__ == '__main__':
    main()