# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:35:14 2021

@author: RyanMcKiernan
"""

def pres_plus_vp(pres_file, vp_file, outfile):
    with open(outfile,'w') as f_out:
        with open(pres_file,'r') as f:
            for line in f:
                f_out.writelines(line)
                
        f_out.writelines('\n')
        
        with open(vp_file, 'r') as f:
            for line in f:
                f_out.writelines(line)
                
                