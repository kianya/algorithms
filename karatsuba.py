#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:22:45 2022

@author: akirichenko
"""
import math


def karatsuba_multiply(x, y):
    """Fast algotrithm for multipling two numbers"""
    
    # Выход из рекурсии
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    
    # Добавляем незначимые нули
    if len(x) % 2 == 1:
        x = '0' + x
    
    # Формируем числа одинаковой длины
    while len(x) != len(y):
        if len(x) < len(y):
            x = '0' + x 
        else:
            y = '0' + y
            
    
    n = len(x)
    i = math.ceil(n/2)
    
    a = x[0:i]
    b = x[i:n]
    c = y[0:i]
    d = y[i:n]
    
    a_x_c = karatsuba_multiply(a, c)
    b_x_d = karatsuba_multiply(b, d)
    
    a_pl_b_x_c_pl_d = karatsuba_multiply(str(int(a)+int(b)), str(int(c) + int(d)))
    ad_x_bc = a_pl_b_x_c_pl_d - a_x_c - b_x_d
    
    return a_x_c * 10**n + ad_x_bc * 10**math.ceil(n/2) + b_x_d


if __name__ == "__main__":
    a = "1221"
    b = "1112"
    res = karatsuba_multiply(a, b)
    print(res)
    
    
    
