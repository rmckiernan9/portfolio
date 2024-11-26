# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:25:15 2021

@author: RyanMcKiernan
"""

def states_w_n_justices(files, filej, n):
    
    with open(files,'r') as s:
        states = 0 #Counts the number of states that match n
        for lines in s:
            datas = lines.split(',')
            count = 0 #Counts the number of justices in a state
           
            with open(filej,'r') as j:
                for linej in j: 
                    dataj = linej.split(',')
                    
                    #Checks for a state match between the two files
                    if dataj[3] == datas[1]: 
                        count += 1
                        
                #Checks if the number of justices in a state matches input n
                if count == n:
                    states += 1
                    
    return states
    