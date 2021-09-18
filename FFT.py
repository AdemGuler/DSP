# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:44:30 2021

@author: adem
"""

import numpy as np
from numpy import sin,pi, arange
from numpy.fft import fft
import matplotlib.pyplot as plt

fs = 100.

n = np.arange(10*fs)

t = n/fs

x = sin(2*pi*t**2 + 10*pi*t)

#plt.plot(t,x)

#Windowing
#1st : 0-99
#2st : 100-199
#10th : 

m = 10
NWin = 100
indices = arange((m-1)*NWin, m*NWin)
winX = x[indices]
#plt.plot(indices,winX)
plt.plot(abs(fft(winX)))
plt.xlim(0,50)
