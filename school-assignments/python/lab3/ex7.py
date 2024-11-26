# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:54:27 2021

@author: RyanMcKiernan
"""

def life(state, gen):

    if gen > 0:

        p = 0
        while p < gen:
            
            #Creates an array that marks a 1 if the state changes in a gen
            change = []
            for m in range(len(state)):
                row = []
                for n in range(len(state[m])):
                    row.append(0)
                change.append(row)
            
            for i in range(len(state)):
                for j in range(len(state[i])):
                    y = len(state)-1 #Last row index
                    x = len(state[i])-1 #Last column index
                    
                    #Upper left corner (3 neighbors)
                    if (i == 0) and (j == 0):
                        n = state[i][j+1]+state[i+1][j]+state[i+1][j+1]
                    #Upper right corner
                    elif (i == 0) and (j == x):
                        n = state[i][j-1]+state[i+1][j]+state[i+1][j-1]
                    #Lower left corner
                    elif (i == y) and (j == 0):
                        n = state[i-1][j]+state[i][j+1]+state[i-1][j+1]
                    #Lower right corner
                    elif (i == y) and (j == x):
                        n = state[i-1][j]+state[i][j-1]+state[i-1][j-1]
                    #Top row non-corner (5 neighbors)
                    elif (i == 0):
                        n = state[i][j-1]+state[i][j+1]+state[i+1][j-1]+\
                            state[i+1][j]+state[i+1][j+1]
                    #Bottom row non-corner
                    elif (i == y):
                        n = state[i][j-1]+state[i][j+1]+state[i-1][j-1]+\
                            state[i-1][j]+state[i-1][j+1]
                    #Left column non-corner
                    elif (j == 0):
                        n = state[i-1][j]+state[i+1][j]+state[i-1][j+1]+\
                            state[i][j+1]+state[i+1][j+1]
                    #Right column non-corner
                    elif (j == x):
                        n = state[i-1][j]+state[i+1][j]+state[i-1][j-1]+\
                            state[i][j-1]+state[i+1][j-1] 
                    #Any non edge square (8 neighbors)
                    else:
                        n = state[i-1][j] + state[i+1][j] + state[i][j+1] +\
                            state[i][j-1] + state[i-1][j-1] + state[i-1][j+1]\
                                + state[i+1][j-1] + state[i+1][j+1]
                            
                    #Checks the rules, notes if state should be changed    
                    if state[i][j] == 1:
                        if (n < 2) or (n > 3):
                            change[i][j] = 1
                    elif state[i][j] == 0:
                        if n == 3:
                            change[i][j] = 1
            
            #Re-iterates and changes the cell
            for k in range(len(state)):
                for l in range(len(state[k])):
                    if (change[k][l] == 1) and (state[k][l] == 0):
                        state[k][l] = 1
                    elif (change[k][l] == 1) and (state[k][l] == 1):
                            state[k][l] = 0
                            
            p += 1
    
    return state
