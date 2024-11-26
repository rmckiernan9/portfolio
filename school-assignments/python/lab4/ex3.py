# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 01:09:53 2021

@author: RyanMcKiernan
"""

import numpy as np

def final_inventory(init_inv,sales):
    final_inv = np.subtract(init_inv,sales)
    return final_inv