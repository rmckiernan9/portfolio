# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:05:50 2021

@author: RyanMcKiernan
"""

#List comprehension syntax

#1. List of squares
squares = []
for i in range(9):
    squares.append(i**2)
    
squares = [i**2 for i in range(9)]

#2. Unit conversion
temps_c = [7,1,3,0,4]

temps_f = []
for t in temps_c:
    temps_f.append(t*1.8 + 32)
    
temps_f = [t*1.8 + 32 for t in temps_c]

#3. Numbers divisible by 3
by_3 = []
for n in range(20):
    if n % 3 ==0:
        by_3.append(n)
        
by_3 = [n for n in range(20) if n%3==0]

#4. Battleship
grid = []
for row in range(65,75):
    for col in range(1,11):
        grid.append((chr(row),col))

    #as a list comprehension
grid = [(chr(row),col) for row in range(65,75) for col in range(1,11)]

#5. multiplication table
table = []
for i in range(1,10):
    row = []
    for j in range(1,10):
        row.append(i*j)
    table.append(row)

    #as a list of comprehensions
    [[i*j for j in range(1,10)] for i in range(1,10)]

#6. subtract two lists, wieghts of participant in diet study
start_wts = [146,166,157,159,153]
end_wts = [142,166,159,155,145]

gl = [] 
for i in range(len(start_wts)):
    gl.append(start_wts[i]-end_wts[i])
    
    #using zip()
    for w in zip(start_wts,end_wts):
        gl.append(w[0]-w[1])
        
        #using zip() method 2
        gl = []
        for start, end in zip(start_wts,end_wts):
            gl.append(start-end)
           
gl = [start-end for start,end in zip(start_wts,end_wts)]

 #Dictonaries
def word_frequency(s):
    freq = {}
    for w in s:
        freq[w] = freq.get(w,0) + 1
        #if w in freq:
         #   freq[w] += 1
        #else:
         #   freq[w] = 1
    return freq
           
def most_freq(d):
    max_count = max(d.values())
    freq_words = [w for w, f in d.items() if f==max_count] 
    return freq_words

#dictonary comprehension implementation
def word_freq(s):
    return{w: s.lower().split().count(w) for w in s.lower().split()}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            