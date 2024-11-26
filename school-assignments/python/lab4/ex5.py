# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 02:09:40 2021

@author: RyanMcKiernan
"""

import numpy as np

def sales_for_store(qfile,pfile,store_id):
    q = np.loadtxt(qfile,delimiter=',')
    p = np.loadtxt(pfile,delimiter=',')
    
    #Matches store ID with corresponding row from sales_qty
    store_sales = np.array(q[store_id-1]).astype(float)
    
    sales = store_sales * p
    
    return np.sum(sales)
