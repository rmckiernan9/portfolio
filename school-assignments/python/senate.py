# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:17:23 2021

@author: RyanMcKiernan
"""

def state_for_senator(filename,name):
    with open(filename,'r') as f:
        for line in f:
            data = line.split(',')
            if data[0].lower() == name.lower():
                state = data[1]
   
    return state