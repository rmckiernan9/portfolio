# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:27:13 2021

@author: RyanMcKiernan
"""

hrswrkd = float(input('Please enter the number of hours worked: '))
hrwage = float(input('Please enter the hourly wage: '))

#Calculates the pay with the cases of working/not working overtime
if hrswrkd > 40:
    pay = (hrwage*40)+((1.5*hrwage)*(hrswrkd-40))
else:
    pay = hrwage*hrswrkd
    
print('Gross pay is ${0:.2f}'.format(pay))
