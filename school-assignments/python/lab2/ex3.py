# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:32:41 2021

@author: RyanMcKiernan
"""
#This function calculates the total and outputs a grade checking the cases.
def assign_grade(exam,lab,quiz,pc,fp,asmt):
    grade = ""
    total = lab + exam + quiz + fp + pc + asmt
    if (total >= 930):
        grade = "A"
    elif (total >= 900 and total <= 929):
        grade = "A-"
    elif (total >= 870 and total <= 899):
        grade = "B+"
    elif (total >= 830 and total <= 869):
        grade = "B"
    elif (total >= 800 and total <= 829):
        grade = "B-"
    elif (total >= 770 and total <= 799):
        grade = "C+"
    elif (total >= 730 and total <= 769):
        grade = "C"
    elif (total >= 700 and total <= 729):
        grade = "C-"
    elif (total >= 670 and total <= 699):
        grade = "D+"
    elif (total >= 600 and total <= 669):
        grade = "D"
    elif (total <= 599):
        grade = "F"
    
    if (lab>240 or exam>250 or quiz>240 or fp>100 or pc>120 or asmt>50):
        grade = "NR"
        
    return grade
    