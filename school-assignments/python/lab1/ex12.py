# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:41:34 2021

@author: RyanMcKiernan
"""

cc = int(input('Enter precentage cloud cover: '))

#Checks the conditional cases and prints the corresponding result
if (cc >= 0) & (cc <= 30):
    print('Clear')
elif (cc >= 31) & (cc <= 70):
    print('Partly cloudy')
elif (cc >=71) & (cc <= 99):
    print('Mostly cloudy')
elif (cc == 100):
    print('Overcast')
else:
    print('Not a valid input')
