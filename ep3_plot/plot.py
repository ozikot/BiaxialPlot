import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():

    # CSVファイル読み込み
    df = pd.read_csv('..//csv_file//merged.csv')

    # 描画するデータの時間範囲を04:00:00~04:19:59に設定します（お互いのグラフ線を区別しているので見やすくするため）
    # and ではなく &
    df = df[('2018-09-01 04:00:00'<= df['Time']) & (df['Time'] < '2018-09-01 04:20:00')]

    ax = df.plot(secondary_y=['Temperature'], figsize=(20, 5), style=['-', '-.'], grid=False, fontsize=15)

    # 各列の要約統計量
    desc = df.describe()

    # 左y軸のラベル
    ax.set_ylabel('BPM', fontsize=15)
    
    # 右y軸のラベル
    ax.right_ax.set_ylabel('Temperature', fontsize=15)

    # x軸のラベル
    ax.set_xlabel('Time', fontsize=15)

    # 左y軸の描画範囲 余裕を持たせるために下限上限共に-1, +1
    ax.set_ylim(math.floor(desc['BPM']['min']) - 1, math.ceil(desc['BPM']['max']) + 1)

    # 右y軸の描画範囲
    ax.right_ax.set_ylim(math.floor(desc['Temperature']['min']) - 1, math.ceil(desc['Temperature']['max']) + 1)

    # x軸の描画範囲
    start_idx = list(df.query('Time == "2018-09-01 04:00:00"').index)[0]
    end_idx = list(df.query('Time == "2018-09-01 04:19:59"').index)[0]
    ax.set_xlim(start_idx, end_idx)

    # グリッドの調整　両y軸のメモリの数をそろえればグリッドを引くのは片方だけに設定すればよい
    ax.grid(True, which='both', linestyle=':')
    ax.set_yticks(np.linspace(math.floor(desc['BPM']['min']) - 1, math.ceil(desc['BPM']['max']) + 1, 8))
    ax.right_ax.set_yticks(np.linspace(math.floor(desc['Temperature']['min']) - 1, math.ceil(desc['Temperature']['max']) + 1, 8))

    plt.show()


if __name__ == '__main__':
    main()