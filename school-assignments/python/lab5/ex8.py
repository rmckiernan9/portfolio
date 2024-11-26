# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:10:46 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def states_w_n_vowels(file,n):
    data = pd.read_csv(file,names=['state', 'abbrev', 'area', 'pop'])
    states = pd.Series(data['state'])
    
    #Detects if there's a unique vowel in the state
    states_a = states.str.lower().str.contains('a',regex=False)
    states_e = states.str.lower().str.contains('e',regex=False)
    states_i = states.str.lower().str.contains('i',regex=False)
    states_o = states.str.lower().str.contains('o',regex=False)
    states_u = states.str.lower().str.contains('u',regex=False)
    
    #Creates a dataframe that can sum the number of unique vowels
    vowels = pd.concat([states_a,states_e,states_i,states_o,states_u]\
                       ,axis=1)
    vowels_sum = vowels.sum(1)
    states_match = np.where(vowels_sum == n)
    
    return np.asarray(states.iloc[states_match])
