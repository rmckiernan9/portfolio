# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:55:43 2021

@author: RyanMcKiernan
"""

def appointed_by(file, name):
    with open(file,'r') as f:
        early = 2021 #Will serve as the range of years returned
        late = 1776 #Returns these values if data not found
        for line in f:
            data = line.split(',')
            #Checks if presidents name contains string
            if name.lower() in data[2].lower(): 
                if int(data[4]) < early:
                    early = int(data[4]) #Checks if there's an earlier year
                if int(data[4]) > late:
                    late = int(data[4]) #Checks if there's a later year
        
        return(early,late)
                