# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:31:10 2021

@author: RyanMcKiernan
"""
#This function compares each letters to see if they're in alphabetical order.
def is_sorted(file):
    result = True
    for i in range(len(file)-1):
        if file[i] > file[i+1]:
            result = False
    
    return result
