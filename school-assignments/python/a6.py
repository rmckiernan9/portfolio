# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:17:59 2021

@author: RyanMcKiernan
"""

import mysql.connector as sql
import pandas as pd
import numpy as np

c = sql.connect(host='localhost',database='invoices',user='root',password='46985tkosFbs')

#Exercise 1
def gl_book_accounts(c):    
    cmd = pd.read_sql('SELECT * FROM general_ledger_accounts' + 
                       ' WHERE account_description like \'%book%\'' +
                       ' or account_description like \'%books%\'',c,\
                           index_col='account_number')
    return cmd

#Exercise 2
def sql_anomalies(c):
    cmd = (' WITH avg_amt AS' +
           ' (SELECT line_item_amt, account_description, invoice_number,' +
           ' AVG(line_item_amt) OVER(PARTITION BY account_description) AS avg_amt' +
           ' FROM invoice_line_items as L' +
           ' JOIN general_ledger_accounts AS A USING (account_number)' +
           ' JOIN invoices AS I using (invoice_id))' +
           ' SELECT line_item_amt, account_description, invoice_number' +
           ' FROM avg_amt' +
           ' WHERE line_item_amt > avg_amt')
    
    return pd.read_sql(cmd,c)
        
def pd_anomalies(c):
    invoices_df = pd.read_sql('SELECT * FROM invoices',c,index_col='invoice_id')
    line_items_df = pd.read_sql('SELECT * FROM invoice_line_items',c)
    accounts_df = pd.read_sql('SELECT * FROM general_ledger_accounts',c,index_col='account_number')
    
    avg_amts = line_items_df.groupby(['invoice_id','account_number']).sum()\
        .reset_index().groupby('account_number').mean()['line_item_amt']

    line_items_2 = pd.merge(line_items_df,avg_amts,on='account_number')
    above_avg = line_items_2[line_items_2['line_item_amt_x'] > line_items_2['line_item_amt_y']]
    final = pd.merge(above_avg,invoices_df,on='invoice_id')
    final = pd.merge(final,accounts_df,on='account_number')
    
    return final[['invoice_number','account_description','line_item_amt_x']]

#Timeit sql_anomalies: 2.22 ms ± 67.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
#Timeit pd_anomalies: 21.8 ms ± 1.55 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
#The SQL one appeared to run significantly faster than the pandas one, likely
#due to the calculations that are needed to complete the task.

c.close()      

#Exercise 3
q=sql.connect(host='localhost',database='a6',user='root',password='46985tkosFbs')

def states_w_n_justices(q,file,n):
    
    n_just = pd.read_sql('SELECT state, COUNT(state) FROM justice GROUP BY state',q)
    states = pd.read_csv(file,header=None,names=['state','abv','area','pop'])
    states_2 = pd.merge(n_just,states,how='right',left_on='state',right_on='abv')
    states_2['COUNT(state)'] = states_2['COUNT(state)'].fillna(0)
    states_n = states_2[states_2['COUNT(state)'] == n]
    
    return states_n['state_y'].tolist()
    
#Exercise 4
def rank_diff_sql(q,year):

    rank_w_profit = pd.read_sql('SELECT `Year`, `Rank`, Company, revenue,' +
                               ' profit, RANK() OVER(PARTITION BY `Year`' +
                               ' ORDER BY profit DESC) as year_rank' +
                               ' FROM fortune500',q)
    year_ranks = rank_w_profit[rank_w_profit['Year'] == year]
    year_ranks['rankdiff'] = abs(year_ranks['Rank']-year_ranks['year_rank'])
    diff_max = year_ranks['rankdiff'].max()
    comps = year_ranks.loc[year_ranks['rankdiff'] == diff_max]
    

    return np.asarray(comps['Company'])

q.close()
