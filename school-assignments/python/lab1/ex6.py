# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:46:00 2021

@author: RyanMcKiernan
"""

ah = int(input('Enter time 1 hours: '))
am = int(input('Enter time 1 minutes: '))
bh = int(input('Enter time 2 hours: '))
bm = int(input('Enter time 2 minutes: '))

#Combines the 2 hour/minute times into one time respectively
hours = ah + bh
minutes = am + bm

#Checks to see if the number of minutes exceeds 60, adds to hour if so
if minutes >= 60:
    hours = hours + 1
    minutes = minutes % 60

print('Total time is {0}:{1}'.format(hours,minutes))
