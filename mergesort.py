#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:02:45 2022

@author: akirichenko
"""

import math


def merge(b, c):
    """Merge two arrays and return one"""
    
    if len(c) == 0 or len(b) == 0:
        return b + c
    
    i = 0
    j = 0
    d = []
    
    n = len(b) + len(c)
    for k in range(n):
        try:
            if b[i] < c[j]:
                d.append(b[i])
                i = min(i+1, len(b)) 
            else:
                d.append(c[j])
                j = min(j+1, len(c))
        except:
            if i == len(b):
                d.extend(c[j:len(c)])
            elif j == len(c):
                d.extend(b[i:len(b)])
            break
    
    return d


def mergesort(a):
    """Sort array"""
    len_a = len(a)
    
    # Edge case
    if len_a < 2:
        return a
    
    i = math.ceil(len_a/2)
    
    # Recursive call for sort two array parts
    b = mergesort(a[0:i])
    c = mergesort(a[i:len_a])
    
    # Merge sorted arrays
    d = merge(b, c)
    print(d)
    
    return d


if __name__ == "__main__":
    a = "8435429573948"
    mergesort(a)
    