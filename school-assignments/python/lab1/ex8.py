# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:16:55 2021

@author: RyanMcKiernan
"""

yr = int(input('Enter year: '))

#Checks if the year is divisible by 4 and the special case of centennial years
if yr % 4 == 0:
    if (yr % 100 == 0) & (yr % 400 != 0):
        print('{0} is a not leap year'.format(yr))
    else:
        print('{0} is a leap year'.format(yr))
else:
    print('{0} is a not leap year'.format(yr))
    
    