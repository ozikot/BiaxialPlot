# 体表温度データのTimeに格納されている値を心拍のTimeと同じフォーマットに変更

import pandas as pd
import matplotlib.pyplot as plt

def change_format(value):
    value /= 10 ** 6
    hour = str(int(value // 3600)).zfill(2)
    value %= 3600
    minu = str(int(value // 60)).zfill(2)
    seco = str(int(value % 60)).zfill(2)
    return '{}:{}:{}'.format(hour, minu, seco)

def main():
    # 体表温度のCSVファイルを読み込む
    df_tm = pd.read_csv('..//temp_bs.csv')

    df_tm['Time'] = df_tm['Time'].map(lambda t : '2018-09-01 ' + change_format(int(t)))

    print(df_tm)

if __name__ == '__main__':
    main()