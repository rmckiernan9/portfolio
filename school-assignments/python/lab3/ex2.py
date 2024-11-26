# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:00:59 2021

@author: RyanMcKiernan
"""

def classify_eggs(l):
    
    #Creates the initial dictonary
    classy = {'Small':0,'Medium':0,'Large':0,'Extra Large':0,'Jumbo':0}
    for w in l:
       if w >= 1.5:
           if w >= 2.5:
               classy['Jumbo'] += 1
           elif w >= 2.25 and w < 2.5: 
               classy['Extra Large'] += 1
           elif w >= 2 and w < 2.25:
               classy['Large'] += 1
           elif w >= 1.75 and w < 2:
               classy['Medium'] += 1
           else:
               classy['Small'] += 1
              
    #Deletes any keys with no results
    for key in list(classy.keys()):
        if classy[key] == 0:
            del classy[key]
       
    return classy

    