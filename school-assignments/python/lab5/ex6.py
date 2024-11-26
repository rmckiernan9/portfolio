# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:38:23 2021

@author: RyanMcKiernan
"""

import pandas as pd

def tot_pop_density(file):
    d = pd.read_csv(file,header=None)
    pop = d[3].sum()
    area = d[2].sum()
    
    dens = pop / area

    return dens
