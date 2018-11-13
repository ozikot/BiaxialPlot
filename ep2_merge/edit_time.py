# 体表温度データのTimeに格納されている値を心拍のTimeと同じフォーマットに変更

import pandas as pd


def change_format(value):
    # 元データはμsなので10**6で割ってsにします
    value /= 10 ** 6

    # zfill(桁数)で桁数分ゼロ埋めをします
    hour = str(int(value // 3600)).zfill(2)
    value %= 3600
    minu = str(int(value // 60)).zfill(2)
    seco = str(int(value % 60)).zfill(2)
    return '{}:{}:{}'.format(hour, minu, seco)


def main():
    # 体表温度のCSVファイルを読み込む
    df_tm = pd.read_csv('..//csv_file//temp_bs.csv')

    # 時間のフォーマットを直します
    # 時間列に含まれているものに無名関数を適用させます（無名関数の中にchange_format関数を内包）
    df_tm['Time'] = df_tm['Time'].map(lambda t : '2018-09-01 ' + change_format(int(t)))

    # CSVファイルに書き込み
    df_tm.to_csv('..//csv_file//temp_bs_edited.csv', index=False)


if __name__ == '__main__':
    main()