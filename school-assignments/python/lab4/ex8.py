# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:23:14 2021

@author: RyanMcKiernan
"""

import numpy as np

def compare_names_for_years(year1,year2,n):
    y1 = np.genfromtxt(year1, dtype=None, delimiter = ',',encoding='utf-8')
    y2 = np.genfromtxt(year2, dtype=None, delimiter = ',',encoding='utf-8')
    
    #Sorts the lists by frequency of names
    y1_sort = sorted(y1, key=lambda t: t[2])
    y2_sort = sorted(y2, key=lambda t: t[2])
    
    #Gets n number of names
    list1 = np.array((y1_sort[len(y1_sort)-n:len(y1_sort)]))
    list2 = np.array((y2_sort[len(y2_sort)-n:len(y2_sort)]))

    #Gets just the names from the prior list
    names1 = list1["f0"]
    names2 = list2["f0"]
    
    #Checks for name matches between the two
    names_match = np.isin(names1,names2)
    
    names_i = np.where(names_match==True)

    return np.sort(names1[names_i])
