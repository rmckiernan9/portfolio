# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:19:03 2021

@author: RyanMcKiernan
"""

deposit = float(input('Enter annual deposit: '))
rate = float(input('Enter rate: '))

#Calculates the annual balance which includes adding the annual deposit
balance = deposit*(1+rate/100)**1
balance = balance + deposit*(1+rate/100)**2
balance = balance + deposit*(1+rate/100)**3

print("After 3 years, balance is: ${0:.2f}".format(balance))
