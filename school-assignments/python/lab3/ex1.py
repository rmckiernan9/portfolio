# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:24:04 2021

@author: RyanMcKiernan
"""

def duplicate_names(names):
    duplicates = []
    seen = [] #Adds names that have already been seen
    for i in range(len(names)):
        if names[i] not in seen:
            seen.append(names[i])
        elif names[i] not in duplicates:
            duplicates.append(names[i])
    
    return duplicates
