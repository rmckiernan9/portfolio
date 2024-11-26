# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:11:20 2021

@author: RyanMcKiernan
"""


import pandas as pd

def highest_avg(file):
    colnames = ['name','team','at bats','hits']
    data = pd.read_csv(file,names=colnames)
    
    #Calculates the average and rounds it
    data['avg'] = (data['hits']/data['at bats'])
    data['avg'] = data['avg'].round(3)
    
    #Sorts the data based on average
    avg_rank = data.sort_values('avg',axis=0,ascending=False)

    #Checks for multiple players with top average
    #top_hitter = pd.DataFrame(avg_rank.iloc[0])
    count = 1
    for i in range(len(data['avg'])-1):    
        if avg_rank.iloc[0]['avg'] == avg_rank.iloc[i+1]['avg']:
            count += 1  
    
    return avg_rank.head(count)
