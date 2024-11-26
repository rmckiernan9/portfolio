# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:33:16 2021

@author: RyanMcKiernan
"""

def starts_with(file, st):
    with open(file,'r') as f:
        count = 0
        for line in f:
            #Casts the string and line both to all lowercase letters
            st = st.lower()
            line = line.lower()
            #Checks if string starts with the line, adds to the count if so
            if line.startswith(st):
                count += 1
    
        return count
    