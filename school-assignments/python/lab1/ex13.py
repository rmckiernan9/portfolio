# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:49:36 2021

@author: RyanMcKiernan
"""

i = float(input('Please enter your initial investment: '))
r = float(input('Please enter your annual interest rate (ex. 2.5): '))
p = float(input('Please enter the monthly annuity payout: '))
s = (1+((r/100)/12)) #represents the 1+rate compounded monthly
month = 0
bal = i #balance = initial investment

#Runs a loop until the balance is less than the annuity
while bal > p:
    bal = (bal*s - p)
    month = month + 1

print('After {0} months, your balance is {1:.2f}.'.format(month,bal))
