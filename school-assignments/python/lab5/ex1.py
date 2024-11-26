# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:27:55 2021

@author: RyanMcKiernan
"""

import pandas as pd

def histogram(text):
    
    #Makes a list of the letters, computes a value count
    s = pd.Series(list(text))
    v = s.value_counts()
    return v.sort_index()