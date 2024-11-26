# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:00:55 2021

@author: RyanMcKiernan
"""

vel = float(input('Enter initial velocity (fps): '))
ht = float(input('Enter initial height (feet): '))
TIME = 3

#Calculates the height after 3 seconds
newht = (-16*(TIME**2))+(vel*TIME)+ht

print('The height after 3 seconds is: {0:.1f} ft'.format(newht))
