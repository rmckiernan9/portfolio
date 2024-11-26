# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:56:17 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def final_results(fileT,fileW):
    teams = pd.read_csv(fileT,header=None)
    
    colnames = ['Jazz','Jets','Owls','Rams','Cubs','Zips']
    data = pd.read_csv(fileW,names=colnames)
    
    wins = (data == 'W').sum(1)
    tm_win = pd.Series([teams,wins])

    return (tm_win,data)

