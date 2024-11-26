# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:38:21 2021

@author: RyanMcKiernan
"""
import math

def letter_grade(mean, s_dev, score)
    if ():
    
    elif 
    
    elif
    
    else:
        
    return grade

def assign_grade(filename):
    scores = []
    with open(filename,'r') as f:
        for line in f:
            scores.append(int(line))
        
    n = len(scores)
    mean = sum(scores) / n
    
    int_sum = 0
    for s in scores:
        int_sum += (s - mean)**2 
    s_dev = math.sqrt(int_sum/n)
    
    grades = list()
    for s in scores:
        grades.append(letter_grade(mean,s_dev,s))
        
    return grades

def a_grade(filename):
    with open(filename,'r'):
        scores = [int(line) for line in r]
        
        