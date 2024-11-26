# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:21:50 2021

@author: RyanMcKiernan
"""

def interpolated_median(grades):
    in_median = 0
    values = []
    #Converts letter grades to GPA values
    for i in range(len(grades)):
        if grades[i] == 'A':
            values.append(4.00)
        elif grades[i] == 'A-':
            values.append(3.67)
        elif grades[i] == 'B+':
            values.append(3.33)
        elif grades[i] == 'B':
            values.append(3.00)
        elif grades[i] == 'B-':
            values.append(2.67)
        elif grades[i] == 'C+':
            values.append(2.33)
        elif grades[i] == 'C':
            values.append(2.00)
        elif grades[i] == 'C-':
            values.append(1.67)
        elif grades[i] == 'D+':
            values.append(1.33)
        elif grades[i] == 'D':
            values.append(1.00)
        elif grades[i] == 'F':
            values.append(0.00)
    
    #Calculate the median
    median = 0
    sort_vals = sorted(values)
    n = len(values)
    index = (n-1) // 2
    if (n % 2):
        median = sort_vals[index]
    else:
        median = ((sort_vals[index] + sort_vals[index+1]) / 2.0)
    
    nl = 0 #Number of grades less than standard median
    ne = 0 #Number of grades equal to standard median
    for v in range(len(values)):
        if values[v] < median:
            nl += 1
        if values[v] == median:
            ne += 1
    
    #Checks case for n2 (or ne) = 0
    if ne == 0:
        in_median = median
    else:
        in_median = median - .167 + (((.5*n)-nl)/ne)*.333
    
    return in_median
