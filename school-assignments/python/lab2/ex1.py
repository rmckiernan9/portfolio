# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:16:03 2021

@author: RyanMcKiernan
"""
#Returns the largest even number in an array
def largest_even(nums):
    count = -1
    for i in range(len(nums)):
        if (nums[i] % 2 == 0 and nums[i] > count):
            count = nums[i]
       
    return count

#Returns the number of two digit numbers in an array
def num_two_digits(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] >= 10 and nums[i] <= 99):
            count += 1
    
    return count

#Returns the number of odd numbers in an array
def num_odd(nums):
    count = 0
    for i in range(len(nums)):
        if (nums[i] % 2 == 1):
            count += 1
            
    return count
