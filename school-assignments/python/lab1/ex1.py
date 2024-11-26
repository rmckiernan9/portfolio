# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:00:56 2021

@author: RyanMcKiernan
"""

name = str(input('Please enter customer name: '))
labhrs = float(input('Please enter labor hours: '))
costs = float(input('Please enter cost of parts and supplies: '))

#These functions calculate the labor/parts costs as well as total costs
labcost = labhrs * 35
prtcost = costs * 1.07
totalcost = labcost + prtcost

print('Customer: {0}'.format(name))
print('Labor cost: {0:.2f}'.format(labcost))
print('Parts cost: {0:.2f}'.format(prtcost))
print('Total cost: {0:.2f}'.format(totalcost))
