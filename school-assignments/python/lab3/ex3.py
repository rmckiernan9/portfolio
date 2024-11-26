# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:11:12 2021

@author: RyanMcKiernan
"""

def justices_appointed_by(file, name):
    pres = []
    with open(file,'r') as f:
        for line in f:
            data = line.split(',')
            if name.lower() in data[2].lower():
                #Factors in the space between first and last names
                pres.append(data[0] + ' ' + data[1])
    
    return pres
