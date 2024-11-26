# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 02:28:48 2021

@author: RyanMcKiernan
"""

import numpy as np

def pct_change(file):
    d = np.loadtxt(file,dtype=str,delimiter=',')
    y1 = np.array(d[:,1]).astype(float)
    y2 = np.array(d[:,2]).astype(float)
    pc = ((y2 / y1)*100)-100

    deg = np.array(d[:,0])
    
    pc_sort = pc[np.argsort(pc)][::-1] 
    deg_sort = deg[np.argsort(pc)[::-1]]
       
    return (deg_sort,pc_sort)