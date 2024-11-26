# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:22:14 2021

@author: RyanMcKiernan
"""

def double_or_1(amt):
    turns = 0
    dollars = 1
    while dollars < amt:
        if amt % 2 == 0:
            amt = amt / 2
        else:
            amt = amt - 1
        turns += 1
    
    return turns
    