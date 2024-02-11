#!/bin/bash

#-------------------------------------------------------
# When running pgbouncer with -l, it generates stats for each thread.
# We concatenate all of them with this script and replace spaces with comma, to generate a csv that we can process with `process_all_data_points.py`
#-------------------------------------------------------

echo "client_id,transaction_no,time,script_no,time_epoch,time_us" > all_results.csv 
cat pgbench_log.* | tr ' ' ',' >> all_results.csv

