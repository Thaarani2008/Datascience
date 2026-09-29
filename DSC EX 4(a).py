# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 07:25:00 2026

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# (a) Car Age vs Resale Value
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([25000, 22000, 19000, 16000, 13000, 10000])

row = stats.pearsonr(x, y)
print(f"Correlation coefficient of X & Y: {row.statistic:.4f}")

plt.scatter(x,y,color='red')
plt.xlabel("Car Age")
plt.ylabel("Resale Value")
plt.title("Car Age vs Resale Value")
plt.grid(True)


# %%

# %%

