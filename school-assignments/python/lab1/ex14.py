# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:30:10 2021

@author: RyanMcKiernan
"""

a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
c = int(input('Enter value for c: '))

#Calculates the determinant
det = (b**2) - 4*a*c

#Checks the 3 cases to determine the number of solutions/calculates it
if det > 0:
    e = (-b + det**0.5)/(2*a)
    f = (-b - det**0.5)/(2*a)
    print('Solution: {0}, {1}'.format(e,f))
elif det == 0: 
    g = (-b + det**0.5)/(2*a)
    print('Solution: {0}'.format(g))  
else:
    print('No solutions.')
