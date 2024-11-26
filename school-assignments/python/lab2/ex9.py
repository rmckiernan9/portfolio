# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:10:09 2021

@author: RyanMcKiernan
"""

def multiples_diff(file,divisor):
    with open(file,'r') as f:
        x = 0
        y = 0
        for line in f:
            value = int(line) #converts text string to int for calculations
            if value % divisor == 0:
                x += value
            else:
                y += value
    
    return abs(x-y)
