# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:05:29 2018

@author: asus1
"""
import numpy as np
from numpy.linalg import inv
a = [1,2,3]
b = np.transpose(a)
A = [[1,0.5,5],[2.3,2,3],[4,1,1.7]]
A1 = inv(A)
c = A1 * b
print(c)
