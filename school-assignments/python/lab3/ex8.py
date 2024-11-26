# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:37:12 2021

@author: RyanMcKiernan
"""

import json

def state_density_rank(integer):
    with open('usstates.json','r') as f:
        data = json.load(f)
        
        #Converts the json file into separate lists
        pops = []
        area = []
        state = []
        for i in data:
            pops.append(data[i]["pop"])
            area.append(data[i]["area"])
            state.append(data[i]["name"])
        
        #Calculates the density for each state
        density = []
        for j in range(len(pops)):
            density.append(int(pops[j])/int(area[j]))
        
        #Combines the lists into a dictonary and sorts in order by density
        combo = {}
        for k in range(len(density)):
            combo[state[k]] = density[k]

        rank = {}
        rank = sorted(combo.items(), key = lambda x: x[1], reverse=True)
        
        value = rank[integer-1][0]
    
    return value
