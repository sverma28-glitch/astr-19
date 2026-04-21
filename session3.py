#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:21:28 2026

@author: sv
"""

def f(x):
    return x**3 + 8

def main():
    x = 9
    result = f(x)
    
    print(result)
    
    if result > 27:
        print("YAY!")

if __name__ == "__main__":
    main()