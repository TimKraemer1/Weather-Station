#!/usr/bin/env python3
import serial
import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

def filter_avg(list):
    return sum(list) / len(list)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    moving_filter = [0, 0, 0, 0, 0]
    moving_filter_ptr = 0
    #data_entries = 0
    
    f = open('tempdata.csv', 'w')
    print('Logging Temperature')
    f.write('time,data\n')
    f.close()
    while True:
        sleep(1)
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            moving_filter[moving_filter_ptr] = float(data)
            moving_filter_ptr += 1
            if moving_filter_ptr > 5:
                moving_filter_ptr = 0
            average_temp = filter_avg(moving_filter)
            timestamp = datetime.datetime.now()
            #timestamp += datetime.timedelta(hours=4)
            timestamp = timestamp.strftime('%Y-%m-%d %H:%M')
            f = open('tempdata.csv', 'a')
            f.write('{},{}\n'.format(timestamp, round(average_temp, 1)))
            f.close()
