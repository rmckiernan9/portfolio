# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:43:41 2021

@author: RyanMcKiernan
"""

def state_density(file,state):
    
#Starts by reading the file, while splitting up the data
    with open(file,'r') as f:
        for line in f:
            data = line.split(',')
            #Checks for a state match, calculates the density
            if data[0].lower() == state.lower():
                density = float(data[3])/float(data[2])
    
    return density
        