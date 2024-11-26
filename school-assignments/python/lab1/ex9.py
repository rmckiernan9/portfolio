# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:49:20 2021

@author: RyanMcKiernan
"""

mt = str(input('Enter military time: '))

#Splits the string into hrs/mins, converts them to ints
hrs=mt[:2]
mins=mt[2:]
hrs=int(hrs)
mins=int(mins)
ampm = "am"

#Checks for the different cases and properly converts them
if hrs > 12:
    ampm = "pm"
    hrs -= 12
elif hrs == 00:
    hrs = 12
    if mins == 0:
        mins = 00
elif hrs == 12:
    ampm = "pm"

print('{0}:{1:02d}{2}'.format(hrs,mins,ampm))
