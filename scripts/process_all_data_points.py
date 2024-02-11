#!/bin/env python

"""
Calculate latency percentiles. 
The resulting file can be then analyzed in the jupyter notebooks.
"""

import pandas as pd

df = pd.read_csv('./all_results.csv')
df['time'] /= 1000
df['time_epoch'] = pd.to_datetime(df['time_epoch'],unit='s')

q = df.quantile([.50,.90,.95,.99])

e = df.groupby('time_epoch').quantile(0.50)
f = df.groupby('time_epoch').quantile(0.90)
g = df.groupby('time_epoch').quantile(0.95)
h = df.groupby('time_epoch').quantile(0.99)

q.to_csv("./all_percentiles.csv")

e.to_csv("./q50.csv")
f.to_csv("./q90.csv")
g.to_csv("./q95.csv")
h.to_csv("./q99.csv")

