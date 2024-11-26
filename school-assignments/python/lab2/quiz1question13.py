# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:01:12 2021

@author: RyanMcKiernan
"""

c1name = input('Enter country 1: ')
c1pop = float(input('Enter country 1 population (thousands): '))
c1gr = float(input('Enter country 1 growth rate (%): '))
c2name = input('Enter country 2: ')
c2pop = float(input('Enter country 2 population (thousands): '))
c2gr = float(input('Enter country 2 growth rate (%): '))

small = min(c1pop, c2pop) #Sets the country with the smaller population
years = 0 #Counts the number of years before a population is passed

#Checks for cases where the populations don't overlap
if (c1gr<c2gr and small == c1pop):
    print("{0}'s population will never exceed {1}'s population at the \
current growth rate.".format(c1name,c2name))
elif (c2gr<c1gr and small == c2pop):
    print("{0}'s population will never exceed {1}'s population at the \
current growth rate.".format(c2name,c1name))
else:
    #Checks for the cases based on which population is bigger/smaller
    if c1pop < c2pop:
        while c1pop < c2pop:
            c1pop = c1pop * (1 + (c1gr/100))
            c2pop = c2pop * (1 + (c2gr/100))
            years += 1
        print("{0}'s population will exceed {1}'s population \
in {2} years.".format(c1name,c2name,years))

    elif c2pop < c1pop:
        while c2pop < c1pop:
            c1pop = c1pop * (1 + (c1gr/100))
            c2pop = c2pop * (1 + (c2gr/100))
            years += 1
        print("{0}'s population will exceed {1}'s population \
in {2} years.".format(c2name,c1name,years))
    
    #Checks for the cases where the populations are equal to each other
    else:
        if c1gr > c2gr:
            print("{0}'s population will exceed {1}'s population \
in 1 year.".format(c1name,c2name))
        elif c2gr > c1gr:
            print("{0}'s population will exceed {1}'s population \
in 1 year.".format(c2name,c1name))
        else:
            print("{0}'s population will be the same as {1}'s \
population.".format(c1name,c2name))
