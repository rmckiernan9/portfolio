# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:59:10 2021

@author: RyanMcKiernan
"""

def words_w_n_vowels(filename, n):
    #in: filename, n
    with open(filename,'r') as f:
        words = 0 #Counts the number of words that match n unique vowels
        for line in f:
            
            #These act as counts for if a vowel is present in a word
            sumVowels = 0
            count_a = 0
            count_e = 0
            count_i = 0
            count_o = 0
            count_u = 0
            for c in range(len(line)):
                if line[c].lower() == 'a':
                    count_a = 1
                elif line[c].lower() == 'e':
                    count_e = 1
                elif line[c].lower() == 'i':
                    count_i = 1
                elif line[c].lower() == 'o':
                    count_o = 1
                elif line[c].lower() == 'u':
                    count_u = 1
                
                sumVowels = count_a + count_e + count_i + count_o + count_u

            if (sumVowels == n):
                words += 1

    return words
