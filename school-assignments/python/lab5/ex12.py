# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:34:40 2021

@author: RyanMcKiernan
"""

import pandas as pd

def total_distance(dm,cities):
    citys = cities
    dist_matrix = pd.read_csv(dm,header=None,names=citys)

    tour_len = 0
    num_cities = len(citys)
    
    shortest_tour = citys[0,1]
    shortest_dist = 0
    
    start_city = citys[0]
    next_city = citys[1]
  
    #Use the two cities next to each other to pull a value and add it to a 
    #distance, then add last and first city together.
        
    return tour_len