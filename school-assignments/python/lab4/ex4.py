# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:17:23 2021

@author: RyanMcKiernan
"""

import numpy as np

def total_sales_change(file):
    d = np.loadtxt(file,dtype=str,delimiter=',')
    
    #Takes the year 1/2 columns and gets the sum of the change
    year1 = np.array(d[:,1]).astype(int)
    year2 = np.array(d[:,2]).astype(int)
    
    change = year2 - year1
    
    return np.sum(change)