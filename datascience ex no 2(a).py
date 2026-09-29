# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:25:33 2026

@author: Admin
"""

a = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"))

if a == 1:
    x = float(input("Enter the first number"))
    y = float(input("Enter the second number"))
    print(f"{x}+{y} =", x+y)

elif a == 2:
    x = float(input("Enter the first number"))
    y = float(input("Enter the second number"))
    print(f"{x}-{y} =", x-y)

elif a == 3:
    x = float(input("Enter the first number"))
    y = float(input("Enter the second number"))
    print(f"{x}*{y} =", x*y)

elif a == 4:
    x = float(input("Enter the first number"))
    y = float(input("Enter the second number"))
    print(f"{x}/{y} =", x/y)
4