#!/bin/bash

> stats.txt

while true; do
        #echo "$(date "+%s") $(cat /proc/`pidof pgbouncer`/stat) $(ps -o pid,pcpu -p `pidof pgbouncer` | tail -n1)" >> stats.txt
        #echo "$(date "+%s") $(cat /proc/`pidof pgcat`/stat) $(ps -o pid,pcpu -p `pidof pgcat` | tail -n1)" >> stats.txt
        echo "$(date "+%s") $(cat /proc/`pidof beam.smp`/stat) $(ps -o pid,pcpu -p `pidof beam.smp` | tail -n1)" >> stats.txt
        sleep 5
done
