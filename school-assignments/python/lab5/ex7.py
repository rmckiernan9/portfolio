# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:08:28 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def longest_names(file):
    lengths = []
    data = pd.read_csv(file,names=['state', 'abbrev', 'area', 'pop'])
    states = pd.Series(data['state'])
    
    #Gets the length of each state name
    lengths = states.str.len()

    #Gets states with maximum length
    max_states = (np.where(lengths == lengths.max()))
  
    return np.asarray(states.iloc[max_states])
