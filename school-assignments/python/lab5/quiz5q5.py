# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 07:54:12 2021

@author: RyanMcKiernan
"""

import pandas as pd

def compare_names_for_years(year1,year2,n):
    df_yr1 = pd.read_csv(year1,names=['Name','Sex','Count'],header=None,delimiter=',')
    df_yr2 = pd.read_csv(year2,header=None,delimiter=',')
    #print(df_yr1)
    
    #Sort the list by name frquency
    year1_sort = df_yr1.sort_index(axis=1)
    year2_sort = df_yr2.sort_index(axis=1)
    #print(year1_sort)
    #Get n number of names
    list1 = pd.Series(year1_sort[len(year1_sort)-n:len(year1_sort)])
    list2 = pd.Series(year1_sort[len(year1_sort)-n:len(year1_sort)])
   # print(len(year1_sort))
    #Get just the names from the prior list
    names1 = list1[0]
    names2 = list2[0]
    #Check for name matches between the two
    names_match = names1.isin([names1,names2])
    names_i = names_match.where(names_match == True)
    
    return names1[names_i].sort_values()
