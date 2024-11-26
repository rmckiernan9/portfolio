# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:03:48 2021

@author: RyanMcKiernan
"""

def payouts(pa,pb,n,bet_digit):
    #Sets up the 2D array chart w/probabilities
    payout = {}
    grid = []
    for i in range(9):
        row = []
        for j in range(n)-1: #Total column will come from sums of each row
            row.append(0.00)
        grid.append(row)
    
    #Idea: Build a grid that gets iterated and
    #for each square, a probability is calculated
    #based upon the probabilities and the number of 
    #contests involved in a given match       
    #Create an expected point value
    
    #Get the probability of each value for each cell in the grid
    for k in range(len(grid)):
        for l in range(len(grid[k])):
            grid[k][l] = ((pa*pb)**l+1)
            #Reformulate the calculation so that it forms a median 
            #and deviates from it and factors in for double digit contests
            #i.e. checks for if say a contest variable ends with "1" to put
            #1 and 11 together.
    
    #Calculate the sums into a list, convert that to a dictonary and return
    sums = []
    for m in range(len(grid)):
        total = 0
        for n in range(len(grid[m])):
            total += grid[m][n]
        sums.append(total*bet_digit) #Multiply by the amount bet
        payout[m] = [total]
    
    return payout