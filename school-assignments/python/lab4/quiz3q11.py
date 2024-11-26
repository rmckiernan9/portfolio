# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 09:05:10 2021

@author: RyanMcKiernan
"""

def bigrams(file):
    with open(file,'r') as f:
        bigram = {}
        phrase = []
        seen = []
        words = []
        for line in f:
            data = line.split() 
            phrase.append(data)
        for w in range(len(phrase)-1):
            for v in range(len(phrase[w])-1):
                if phrase[w][v+1] != len(phrase[w][v+1]):
                    words.append(phrase[w][v] + phrase[w][v+1])
                else:
                    words.append(phrase[w][v+1] + phrase[w+1][0])
        
        for z in range(len(words)):
            if z not in seen:
                seen.append(words[z])
                bigram[words[z]] = 1
            else:
                bigram[words[z]] = bigram.get(words[z],0) + 1

    
    return bigram