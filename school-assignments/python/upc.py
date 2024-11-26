# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:15:42 2021

@author: RyanMcKiernan
"""
#Incorporate string having to be 12 characters
def valid_upc(upc):
    count = 0
    for i in range(len(upc)):
        if i % 2 ==0:
            count += int(upc[i])*3
        else:
            count += int(upc[i])
    
    return count % 10 == 0

    