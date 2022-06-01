# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:39:30 2016

@author: Anuha
"""

import numpy as np
import pylab as pyl

x = np.arange(-5,5,0.01)
y = x**2 + x
pyl.plot(x,y)

pyl.plot(x, x-5)
pyl.plot(x, -(5/2)*x + 2)

