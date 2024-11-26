# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:07:43 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def years_w_no_appointments(file):
    data = pd.read_csv(file,header=None)
    
    appoint_yrs = pd.Series(data[4])
    #print(appoint_yrs)
    minyr = appoint_yrs.min() #Get the first/last year of a judge appointed
    maxyr = appoint_yrs.max() #in order to create a range of all possible yrs

    years = pd.Series(range(minyr,maxyr))
    
    #Gets years without a judge
    years_wojudge = ~years.isin(appoint_yrs)
    
    return years[years_wojudge]
