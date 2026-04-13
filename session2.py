#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:14:40 2026

@author: sv
"""

import numpy as np

float1 = np.random.rand()
float2 = np.random.rand()


print("The floats are", float1, "and", float2)
print("The sum is: ", float1 + float2)
print(type(float1+float2))

int1 = np.random.randint(0, 100)
int2 = np.random.randint(0, 100) 
print("The integers are", int1, "and", int2)
print("The difference is: ",int1-int2)
print(type(int1+int2)) 

int3 = np.random.randint(0, 100)
float3 = np.random.rand()
print(f"The integer is {int3} and the float is {float3}.")
print(f"The product is: {int3*float3}.")
print(type(int3*float3)) 
