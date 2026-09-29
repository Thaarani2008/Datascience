# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:16:22 2026

@author: Admin
"""

import numpy as np
import statistics

a = np.array([12,18,24,18,30,36,42,48,54])

print("Mean =", np.mean(a))
print("Median =", np.median(a))
print("Mode =", statistics.mode(a.tolist()))
print("Variance =", np.var(a))
print("Standard Deviation =", np.std(a))	
print("Minimum =", np.min(a))
print("Maximum =", np.max(a))
print("Range =", np.max(a) - np.min(a))  
z=(24-np.mean(a))/np.std(a)
print("z-sccore=",z)

