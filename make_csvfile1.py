# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# data size
ds = 30000

# Generate heartbeat data with simple random walk
# initial value(p0) = 100
dn = np.random.choice([-1, 1], size=ds)
p0 = 100
swalk = np.cumsum(dn) + p0

# Generate data drame
df = pd.DataFrame({
    'Time' : pd.date_range('2018/09/01 00:00:00', periods=ds, freq='1S'),
    'bpm' : pd.Series(swalk)
})

print(df)