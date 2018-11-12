import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成するデータの行数
ds = 30000

# 幾何ランダムウォークで疑似的な心拍データの生成
dn = np.random.choice([-1, 1], size=ds)
p0 = 100
gwalk = np.cumprod(np.exp(dn * 0.001)) * p0
pd.Series(gwalk).plot()

# データフレームを生成
df = pd.DataFrame({
    'Time' : pd.date_range('2018/09/01 00:00:00', periods=ds, freq='1S'),
    'BPM' : pd.Series(gwalk)
})

# データフレームをCSVファイル形式で保存
df.to_csv('heartbeat.csv', index=None)