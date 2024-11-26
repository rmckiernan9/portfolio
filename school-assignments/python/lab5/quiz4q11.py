# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:00:44 2021

@author: RyanMcKiernan
"""

import numpy as np

def state_density_rank(file,n):

    data = np.loadtxt(file,dtype=str,delimiter=',')
    
    #Gets the population, area columns
    population = data[:,3].astype(float)
    area = data[:,2].astype(float)

    #Calculates the density
    density = population / area
    
    #Sorts the states based on density ranking, largest to smallest
    states_sort = data[np.argsort(density)][::-1]
    
    return states_sort[n-1][0]
