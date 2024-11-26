# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 00:52:33 2021

@author: RyanMcKiernan
"""
import numpy as np
def miles_between(file,fcid,tcid):
    d = np.loadtxt(file,dtype=int,delimiter=',')
    distance = d[fcid-1][tcid-1]
    return distance
