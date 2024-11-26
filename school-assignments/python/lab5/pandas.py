# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:55:50 2021

@author: RyanMcKiernan
"""

import pandas as pd
# Optional / recommended
# from pandas import Series, DataFrame


t = pd.read_csv('train.csv')


# Explore the data
t.head()   # First 5 rows
t.tail()   # Last 5 rows


# Isolate the IsHoliday column
t.IsHoliday
# More general / recommended:
t['IsHoliday']  # returns a Series


# Isolate more than one column
t[['Date', 'Weekly_Sales']]  # returns a DataFrame


# How many holiday weeks are represented in the file?
t['IsHoliday'].sum()


# How many non-holiday weeks are represented in the file?
t['IsHoliday'].count() - t['IsHoliday'].sum()
# A bit better
(t['IsHoliday'] == False).sum()
# Probably the best:
(~t['IsHoliday']).sum()


# How many records do we have for each store?
t['Store'].value_counts()
# Sorted by store number
t['Store'].value_counts().sort_index()
# Sorted by number of records
t['Store'].value_counts().sort_values()
# Sorted by number of records, descending
t['Store'].value_counts().sort_values(ascending=False)


# Entire data frame, sorted by Weekly_Sales
t.sort_values('Weekly_Sales', ascending=False)


# Rank records by Weekly_Sales
t['Weekly_Sales'].rank(method='min', ascending=False).astype(int)
t['rank'] = t['Weekly_Sales'].rank(method='min', ascending=False).astype(int)


# All records with a Weekly_Sales of $600,000 or more
t[t['Weekly_Sales'] >= 600000]


# Total sales at store 13 during holiday weeks
t['Weekly_Sales'][(t['Store'] == 13) & t['IsHoliday']].sum().round(2)
# Another approach, just the same:
t[(t['Store'] == 13) & t['IsHoliday']]['Weekly_Sales'].sum().round(2)


# Add an average daily sales column
t['avg_daily_sales'] = t['Weekly_Sales'] / 7


# Find the record with the maximum weekly sales
t[t['Weekly_Sales'] == t['Weekly_Sales'].max()]


# Minimum amount of weekly sales during a holiday week
# Come back to this one
t[t['Weekly_Sales'] == (t['Weekly_Sales'][t['IsHoliday']].min())]


# Read in the usstates.csv file
s = pd.read_csv('usstates.csv',
                names=['state', 'abbrev', 'area', 'pop'])

# Avoid doing this after the fact. Integrate with read_csv!
# s.columns = ['state', 'abbrev', 'area', 'pop']