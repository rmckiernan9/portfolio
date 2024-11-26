# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:16:40 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def rank_diff(file,year):
    data = pd.read_csv(file,header=0)
    cur_year = data[data['Year']==year] #Data from current year
    
    rank_profit = cur_year.sort_values(['Profit (in millions)'],ascending=\
                                       False)
    rank_profit = rank_profit.drop(rank_profit[rank_profit[\
                    'Profit (in millions)'] == 'N.A.'].index)
    
      
    rank_profit['Profit (in millions)']=rank_profit['Profit (in millions)']\
        .astype(float)

    rank_profit.sort_values(['Profit (in millions)'],ascending=False)

    rank_profit.insert(5,'Profit Rank',range(1,len(rank_profit)+1,1))
    
    rank_difference = abs(rank_profit['Rank']-rank_profit['Profit Rank'])
    rank_profit.insert(6,'RankDiff',rank_difference)
 
    max_diff = rank_difference.max()

    max_comp = rank_profit.loc[max_diff == rank_profit['RankDiff']]
    
    return np.asarray(max_comp['Company'])
