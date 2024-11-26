# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 02:24:14 2021

@author: RyanMcKiernan
"""

import numpy as np

def final_results(tfile,wlfile):
    teams = np.loadtxt(tfile,dtype=str,delimiter=',')
    winloss = np.loadtxt(wlfile,dtype=str,delimiter=',')
    
    #Calculates the number of wins for each team
    wins = (winloss == 'W').sum(1)

    teams_sort = teams[np.argsort(wins)[::-1]]
    wins_sort = wins[np.argsort(wins)[::-1]]
    
    return teams_sort,wins_sort

