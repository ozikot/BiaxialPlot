import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成するデータの行数
ds = 30000

# 幾何ランダムウォークで疑似的な心拍データの生成
dn = np.random.choice([-1, 1], size=ds)
p0 = 20
gwalk = np.cumprod(np.exp(dn * 0.001)) * p0
pd.Series(gwalk).plot()

# データフレームを生成
df = pd.DataFrame({
    'Time' : pd.Series([i * 1000000 for i in range(0, ds)]),
    'Temperature' : pd.Series(gwalk)
})

# データフレームをCSVファイル形式で保存
df.to_csv('..//csv_file//temp_bs.csv', index=None)