# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 07:31:03 2026

@author: Admin
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats    

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([55, 60, 65, 70, 75, 80, 85, 90])

row = stats.pearsonr(x, y)
print(f"Correlation coefficient of X & Y: {row.statistic:.4f}")
plt.scatter(x, y,color='red')
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.grid(True)