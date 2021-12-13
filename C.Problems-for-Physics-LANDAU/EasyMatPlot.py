#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:57:38 2021

@author: david
"""

#%%
from pylab import *

#%%
Xmin = -5.
Xmax = +5.
Npoints = 500

DelX = (Xmax - Xmin)/Npoints

x = arange(Xmin, Xmax, DelX)
y = sin(x)*sin(x*x)

print('arange => x[0], x[1], x[499]=%8.2f %8.2f %8.2f' %(x[0], x[1], x[499]))
print('arange => y[0], y[1], y[499]=%8.2f %8.2f %8.2f' %(y[0], y[1], y[499]))

print('\n Doing plotting, look for Figure 1')

xlabel('x')
ylabel('y')
title('f(x) vs x')

text(-1.75, 0.75, 'MatPlotlib \n Example')

plot(x, y, '-', lw = 2)
grid(True)
show()