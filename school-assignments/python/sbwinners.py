# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:58:14 2021

@author: RyanMcKiernan
"""
def sb_winner(filename, n):
    with open(filename,'r') as f:

        for i in range(n-1):
            f.readline()
    
        desired_winner = f.readline().strip()

        return desired_winner
