#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:49:10 2021

@author: david
"""
#%%
from vpython import *

#%%
string = 'blue: sin^2(x), black = cos^2(x), cyan: sin(x)*cos(x)'

graph1 = graph(title = string,
               xtitle = 'x',
               ytitle = 'y',
               background = color.white,
               foreground = color.black)

y1 = gcurve(color = color.blue)
y2 = gvbars(color = color.black)
y3 = gdots(color = color.cyan)

for x in arange(-5, 5, 0.1):
    y1.plot(pos = (x, sin(x)**2))
    y2.plot(pos = (x, cos(x)*cos(x)/3.))
    y3.plot(pos = (x, sin(x)*cos(x)))