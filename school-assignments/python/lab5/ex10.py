# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:13:11 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def new_to_list(file,year):
    data = pd.read_csv(file,header=0)

    cur_year = data[data['Year']==year] #Data from current year
    past_year = data[data['Year']==year-1] #Data from prior year

    #Determines the companies that are new to the list
    is_new = ~cur_year['Company'].isin(past_year['Company'])

    new_list = cur_year[is_new]
    
    return np.asarray(new_list['Company'].sort_values())
