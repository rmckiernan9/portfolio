# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:39:56 2021

@author: RyanMcKiernan
"""
def translate(dfile, phrase, startlang, endlang):
    from_index = 0 #These will index the languages in the csv file
    to_index = 0
    
    #Checks for where those indexes are
    with open(dfile,'r') as f:
        head = f.readline()
        data = head.split(',')
        i = 0
        while i < len(data):
            if data[i].strip() == startlang:
                from_index = i
            elif data[i].strip() == endlang:
                to_index = i
            i += 1
        f.close()
    
        #Takes the period out of the phrase for translating purposes
        period = False
        if phrase[-1] == '.':
            phrase1 = phrase.replace('.','')
            period = True
            
        #Splits the phrase into words, store in a list
        if period == True:
            word_list = phrase1.split()
        else:
            word_list = phrase.split()

        j = 0
        while j < len(word_list):
            with open(dfile,'r') as g:
                next(g)
                for line in g:
                    n_data = line.split(',')
                    
                    #Case for capital letter, rest lowercase
                    if (word_list[j][0] == n_data[from_index][0]) and\
                        (word_list[j][1] == n_data[from_index][1].strip()\
                         .lower()):
                            word_list[j] = n_data[to_index][0] + n_data\
                                [to_index][1:len(n_data[to_index])]\
                                .strip().lower()
                    
                    #Case for all lowercase letters           
                    elif word_list[j]==n_data[from_index].strip().lower():
                        word_list[j] = n_data[to_index].strip().lower()
                            
                    #Case for all uppercase letters
                    elif word_list[j] == n_data[from_index].strip():
                        word_list[j] = n_data[to_index].strip()
                        
                j += 1
        
        #Combines the list items into a string and adds back the period.
        if period == True:
            new_phrase = " ".join(word_list) + '.'
        else:
            new_phrase = " ".join(word_list)
        
    return new_phrase
