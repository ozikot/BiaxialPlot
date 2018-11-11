# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data size
ds = 30000

"""
# Generate heartbeat data with simple random walk
# initial value(p0) = 100
dn = np.random.choice([-1, 1], size=ds)
p0 = 100
swalk = np.cumsum(dn) + p0
"""

# Generate heartbeat data with geometric random walk
# initial value(p0) = 100
dn = np.random.choice([-1, 1], size=ds)
p0 = 100

gwalk = np.cumprod(np.exp(dn * 0.01)) * p0
pd.Series(gwalk).plot()
plt.show()

# Generate data frame
df = pd.DataFrame({
    'Time' : pd.date_range('2018/09/01 00:00:00', periods=ds, freq='1S'),
    'bpm' : pd.Series(gwalk)
})

df.to_csv('test.csv')