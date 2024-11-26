# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 01:09:33 2021

@author: RyanMcKiernan
"""

import numpy as np

def rankings_for(file,school):
    d = np.loadtxt(file,dtype=str,delimiter=',')
    length = int(d.size)
    row = int(d[0].size)
    n = []
    for i in range(int(length/row)):
        for j in range(row):
            if d[i][j] == school:
                n.append(d[i][0])
    
    return np.asarray(n)