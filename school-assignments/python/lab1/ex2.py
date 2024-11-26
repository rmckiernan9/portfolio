# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:26:12 2021

@author: RyanMcKiernan
"""

miles = float(input('Enter miles: '))
yards = float(input('Enter yards: '))
feet = float(input('Enter feet: '))
inches = float(input('Enter inches: '))

#Converts the input units into a single unit of measurement, inches
dist = (63360*miles)+(36*yards)+(12*feet)+inches
centimeters = dist/.3937

#Calculates each new unit, puts the remainder back in centimeters
kilometers = centimeters // 100000
centimeters = centimeters % 100000

meters = centimeters // 100
centimeters = centimeters % 100

print('The metric length is:')
print('{0:.0f} kilometers'.format(kilometers))
print('{0:.0f} meters'.format(meters))
print('{0:.1f} centimeters'.format(centimeters))
