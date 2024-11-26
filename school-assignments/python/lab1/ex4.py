# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:08:18 2021

@author: RyanMcKiernan
"""

bike = float(input('Enter hours cycling: '))
run = float(input('Enter hours running: '))
swim = float(input('Enter hours swimming: '))

#Calculates the amount of calories burned overall and converts to pounds
cals = (200*bike)+(475*run)+(275*swim)
lbs = cals / 3500

print('Total pounds lost: {0:.1f}'.format(lbs))
