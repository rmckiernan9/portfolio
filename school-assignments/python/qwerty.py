# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:57:22 2021

@author: RyanMcKiernan 
"""
#def is_qwerty(word):
 #   for c in word:
  #      if c not in 'qwertyuiop':
   #         return False
    #return True
    
def is_qwerty(word):
    qwerty_word = True
    
    for c in word:
        if c not in 'qwertyuiop':
            qwerty_word = False
    
    return qwerty_word
