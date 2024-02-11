#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 binidxaba <binidxaba@noemail.com>
#
# Distributed under terms of the MIT license.

"""
Parses the output of the PgBench program when executed without the -C option.

Two csv files are generated:
    1) `progress.csv` contains the stats generated with the `-P <interval>` option.
    2) `summary.csv` contains the summarized stats as printed by PgBench.

The csv files can then be processed in the jupyter notebook.
"""
import re
import sys
import pandas as pd

expressions = [
        { "label" : "txn_type",       "cmd" : None, "regex" : r"transaction type: <builtin: (\.+)>" },
        { "label" : "scaling_factor", "cmd" : None, "regex" : r"scaling factor: (\d+)" },
        { "label" : "query_mode",     "cmd" : None, "regex" : r"query mode: (\s+)" },
        { "label" : "num_clients",    "cmd" : None, "regex" : r"number of clients: (\d+)" },
        { "label" : "num_threads",    "cmd" : None, "regex" : r"number of threads: (\d+)" },
        { "label" : "max_num_tries",  "cmd" : None, "regex" : r"maximum number of tries: (\d+)" },
        { "label" : "duration",       "cmd" : None, "regex" : r"duration: (\d+) s" },
        { "label" : "num_txns",       "cmd" : None, "regex" : r"number of transactions actually processed: (\d+)" },
        { "label" : "num_failed_txns","cmd" : None, "regex" : r"number of failed transactions: (\d+) \(.*%\)" },
        { "label" : "latency_avg",    "cmd" : None, "regex" : r"latency average = (\d+\.\d+) ms" },
        { "label" : "latency_stddev", "cmd" : None, "regex" : r"latency stddev = (\d+\.\d+) ms" },
        { "label" : "conn_time",      "cmd" : None, "regex" : r"initial connection time = (\d+\.\d+) ms" },
        { "label" : "tps",            "cmd" : None, "regex" : r"tps = (\d+\.\d+) \(without initial connection time\)" },
]

progress_exp = r"progress: (\d+\.\d+) s, (\d+\.\d+) tps, lat (\d+\.\d+) ms stddev (\d+\.\d+), (\d+) failed"
progress_cmd = re.compile(progress_exp)

fname_exp = r"(\S+)_(\d+).out"
fname_cmd = re.compile(fname_exp)

for exp in expressions:
    cmd = re.compile(exp['regex'])
    exp['cmd'] = cmd

all_files = sys.argv[1:]

stats = []
summary = []

for fname in all_files:

    m = fname_cmd.match(fname)
    if m is None:
        continue

    pooler = m.group(1)
    clients = m.group(2)

    with open(fname, "r") as f:
        contents = f.readlines()

    for i,line in enumerate(contents):
        line = line.strip()
        #print(f"{i} : {line}")
        
        m = progress_cmd.match(line)
        if m is None:
            continue

        item = {
                "pooler":           pooler,
                "num_clients":      clients,
                "progress":         m.group(1),
                "tps":              m.group(2),
                "latency":          m.group(3),
                "latency_stddev":   m.group(4),
                "failed":           m.group(5)
                }
        stats.append(item)


    item = {
            "pooler"    :   pooler
            }
    for i,line in enumerate(contents):
        line = line.strip()
        #print(f"{i} : {line}")
        
        for exp in expressions:
            m = exp['cmd'].match(line)
            if m is None:
                continue

            item[exp['label']] = m.group(1)

    summary.append(item) 

print(stats)
df_progress = pd.DataFrame(stats)
df_progress.to_csv("progress.csv", index=False)

print(summary)
df_summary = pd.DataFrame(summary)
df_summary.to_csv("summary.csv", index=False)

