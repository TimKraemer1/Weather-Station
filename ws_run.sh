#!/bin/bash

# This bash script starts the webserver to display sensor data

current_directory=$(pwd)
cd web_server
(python3 main.py > stdout) >& stderr &
cd $current_directory
