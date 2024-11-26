# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:23:00 2021

@author: RyanMcKiernan
"""

#Boolean indexing
#----------------
import numpy as np
import random

lakes = np.array(["Huron","Ontatio","Michigan","Erie","Superior"])
lake_areas = np.array([23000,8000,22000,10000,32000])

#The number of great lakes
len(lakes) #Avoid this
lakes.size #Do this instead (numpy arrays work better with numoy functions)

#The area of the 5th lake of the list
lake_areas[4]

#The largest area in lake_areas
max(lake_areas) #avoid this
lake_areas.max()

#The total area of all 5 lakes
sum(lake_areas) #avoid this
lake_areas.sum()

#All area figures greater than 22000 sqmi
lake_areas > 22000
lake_areas[lake_areas > 22000] 

#The name of the lake with the largest area
lakes[lake_areas == lake_areas.max()]

#The name of all lakes smaller than 22000 sqmi
lakes[lake_areas < 22000]

#How many lakes have an area smaller than 22000 sqmi
lakes[lake_areas < 22000].size

#The area of Lake Michigan
lake_areas[lakes == "Michigan"][0]

#The names of all lakes in alphabetical order
lakes.sort() #Sorts the array in place, don't do this!
np.sort(lakes)

#The names of all lakes in order by area, largest to smallest
lakes[np.argsort(lake_areas)][::-1]

#Using timeit for performance analysis
large_list = [random.randint(1,100) for i in range(100000)]
large_arr = np.random.standard_normal(100000)

#
def lessthann:
    np.loadtxt











