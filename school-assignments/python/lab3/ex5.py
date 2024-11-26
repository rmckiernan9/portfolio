# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:56:30 2021

@author: RyanMcKiernan
"""

def mpg(file):
    mpgs = {} #Dictonary that is returned
    seen = [] #List that keeps track of cars already accounted for
    count = {} #Keeps track of how many of each car we have
    with open(file,'r') as f:
        for line in f:
            data = line.split(',')
            
            #Checks if the car is in the list
            if data[0] not in seen:
                seen.append(data[0])
                data[1] = data[1].strip()
                seen.append(float(data[1]))
                count[data[0]] = 1 #Accounts for first car in list
            #If it is, it takes the two numbers adds them up    
            else:
                for i in range(len(seen)):
                    if data[0] == seen[i]:
                        seen[i+1] = (float(data[1])+(seen[i+1]))
                        count[data[0]] += 1

            index = 0
            countList = list(count.values()) #Converts count to a list
        
        #Gets the average for each type of car based on number of entries
        for k in range(0,len(seen),2):
            seen[k+1] = seen[k+1] / countList[index]
            index += 1
            
        #Converts the list into a dictonary, rounds to one decimal place 
        for j in range(0,len(seen),2):
            mpgs[seen[j]] = round((100 / seen[j+1]),1)
    
    return mpgs
