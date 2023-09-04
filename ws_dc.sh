#!/bin/bash

#This bash script starts the python weather station data collection script and runs it in the background, piping stdout and stderr into their own files

current_directory=$(pwd)

cd python_scripts/DataLoggerSystem

(python3 serial_read.py > stdout) >& stderr &

cd $current_directory


