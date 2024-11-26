# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:37:24 2021

@author: RyanMcKiernan
"""

import json

def avg_temp(cc):
    with open('minneapolis.json','r') as f:
        data = json.load(f)
        data_list = data['list']
        
        sumTemp = 0
        count = 0
        for i in range(len(data_list)):
            if data_list[i]['clouds']['all'] == cc:
                sumTemp += data_list[i]['main']['temp']
                count += 1
        
        #Calculates the needed temperatures, returns none if there aren't
        #any cloud cover matches
        if count > 0:
            avgTemp = sumTemp / count
            tempC = avgTemp - 273.15
            tempF = (tempC*1.8) + 32
            temps = (tempC, tempF)
        else:
            temps = None
            
    return temps
