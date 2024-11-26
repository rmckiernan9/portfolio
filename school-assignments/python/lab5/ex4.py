# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:06:49 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def interpolated_median(file):
    data = pd.read_csv(file,sep=' ',header=None)

    in_median = 0
    values = []
    for i in range(len(data[0])):
        if data[0][i] == 'A':
            values.append(4.000)
        elif data[0][i] == 'A-':
            values.append(3.667)
        elif data[0][i] == 'B+':
            values.append(3.333)
        elif data[0][i] == 'B':
            values.append(3.000)
        elif data[0][i] == 'B-':
            values.append(2.667)
        elif data[0][i] == 'C+':
            values.append(2.333)
        elif data[0][i] == 'C':
            values.append(2.000)
        elif data[0][i] == 'C-':
            values.append(1.667)
        elif data[0][i] == 'D+':
            values.append(1.333)
        elif data[0][i] == 'D':
            values.append(1.000)
        elif data[0][i] == 'F':
            values.append(0.000)
            
    #Converts to a pandas series and calculates the median
    values_series = pd.Series(values)
    median = values_series.median()

    nl = 0 #Number of grades less than standard median
    ne = 0 #Number of grades equal to standard median
    for v in range(len(values_series)):
       if values_series[v] < median:
           nl += 1
       if values_series[v] == median:
           ne += 1
    
    #Checks case for n2 (or ne) = 0
    if ne == 0:
        in_median = median
    else:
        in_median = median - .167 + (((.5*len(values_series))-nl)/ne)*.333
    
    return round(in_median,3)

