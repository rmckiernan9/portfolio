# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:25:24 2021

@author: RyanMcKiernan
"""

strt = float(input('Enter beginning odometer: '))
end = float(input('Enter ending odometer: '))
gal = float(input('Enter gallons: '))

#Calculates the miles per gallon
mpg = (end-strt)/gal

print('Fuel Efficency: {0:.1f} miles per gallon'.format(mpg))
