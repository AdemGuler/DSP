# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:34:54 2021

@author: adem
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import sounddevice as sd



fs = 8000

t = np.arange(3*fs)/fs

signal1 = np.sin(2*np.pi*440*t)

signal2= np.exp(-10*t)


testSignal= signal1*signal2

# =============================================================================
#
# sd.play(signal1,8000)
# plt.plot(t,testSignal)
#
# =============================================================================


R = fs*.4
alpha= 0.1

b = np.hstack((1,np.zeros(int(R-1)),alpha))
a = 1

from scipy.signal import lfilter


output = lfilter(b,a,testSignal)

plt.plot(t,output)

sd.play(output,8000)