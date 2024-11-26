# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:35:17 2021

@author: RyanMcKiernan
"""

n = float(input('Please enter the maximum demoninator: '))

summ = 0
count = 1

#Runs a loop that increments/adds to sum until the max denominator is reached
while count <= n:
    summ = summ + 1/count
    count = count + 1

print('The sum is {0}'.format(summ))
