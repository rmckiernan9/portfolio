# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:24:57 2021

@author: RyanMcKiernan
"""

dscrp = str(input('Description of the item: '))
cost = float(input('Cost of the item: '))
life = float(input('Estimated life of the item in whole years: '))
method = float(input('Depreciation method (1 = straight line, 2 = double declining balance): '))

#Builds the top of the table, prepares output values
print('Depreciation schedule for: {0}'.format(dscrp))
print('Year   Begin    Dep     End ')
beg = cost
dep = 0
end = cost
year = 0

#Breaks it down into the two types,
#loops through each year and fills in the table
if method == 1:
    print('{0:4} {1:7.2f} {2:6.2f} {3:7.2f}'.format(year,beg,dep,end))
    dep = (1/life)*cost
    year +=1
    while year <= life:
        end = end - dep
        print('{0:4} {1:7.2f} {2:6.2f} {3:7.2f}'.format(year,beg,dep,end))
        beg = beg - dep
        year += 1
elif method == 2: 
    print('{0:4} {1:7.2f} {2:6.2f} {3:7.2f}'.format(year,beg,dep,end)) 
    dep = (2/life)*cost
    year +=1
    while year < life:
        end = end - dep
        print('{0:4} {1:7.2f} {2:6.2f} {3:7.2f}'.format(year,beg,dep,end))
        beg = beg - dep
        dep = dep * (1-2/life)
        year +=1
    dep = beg
    end = beg - dep
    print('{0:4} {1:7.2f} {2:6.2f} {3:7.2f}'.format(year,beg,dep,end))
