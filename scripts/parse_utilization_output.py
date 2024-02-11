#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 binidxaba <binidxaba@noemail.com>
#
# Distributed under terms of the MIT license.

"""
Parses a file containing information about system resources and `ps` and
generates a csv file. The resulting file can be analyzed by the jupyter
notebook.
"""
import pandas as pd
import sys

fname = sys.argv[1]

stats = []

with open(fname, "r") as f:
    contents = f.readlines()

for i,line in enumerate(contents):
    line = line.strip()
    tokens = line.split(' ')

    #print(f"{i} : {line}")
    
    item = {
            "ts":     int(tokens[0]),
            "pid":    int(tokens[1]),
            "vsize":  int(tokens[23]),
            "cpu":    float(tokens[54]),
            }
    stats.append(item)


print(stats)
df = pd.DataFrame(stats)
df.to_csv("utilization.csv", index=False)
