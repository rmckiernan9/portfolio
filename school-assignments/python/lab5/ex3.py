# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:05:52 2021

@author: RyanMcKiernan
"""

import numpy as np
import pandas as pd

def duplicates(file):
    names = pd.read_csv(file,sep=" ",header=None,names=['Name'])
    print(names)
    #Makes count on series, returns those > 1
    count = names['Name'].value_counts()
  
    return np.asarray(count.index[count > 1])