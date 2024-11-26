#-*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:12:52 2021

@author: RyanMcKiernan
"""

def correl(file,col1,col2):
    c1i = 0
    c2i = 0
    with open(file,'r') as h:
        corcoef = 0
        #this will look for the correct columns, get indicies
        head = h.readline()
        data = head.split(',')
        i = 0
        while i < len(data):
            if data[i] == col1:
                c1i = i
            elif data[i] == col2:
                c2i = i
            i += 1
        h.close()
        with open(file,'r',encoding='utf-8') as f:
            next(f) #Jumps the header column for calculating coefficients
            X = []
            Y = []
            sumX = 0 #These are the variables that will be used in
            sumY = 0 #the correlation formula below.
            sumXY = 0
            sumX2 = 0
            sumY2 = 0
            numerator = 0
            denom = 0
            for line in f:
                newdata = line.split(',')
                #Checks for blank columns, eliminates those
                if newdata[c1i] !='':
                    X.append(newdata[c1i])
                if newdata[c2i] !='':
                    Y.append(newdata[c2i])
            
            #The part below calculates the variables that are used for the
            #correlation.
            n = len(X)
            for i in range(n):
                X[i] = float(X[i])
                Y[i] = float(Y[i])
                sumX += X[i]
                sumY += Y[i]
                sumXY += (X[i]*Y[i])
                sumX2 += (X[i])**2
                sumY2 += (Y[i])**2

            numerator = ((n*sumXY)-(sumX*sumY))
            denom = (((n*sumX2)-(sumX**2))*((n*sumY2)-(sumY**2)))**0.5

            corcoef = numerator / denom

        return corcoef


