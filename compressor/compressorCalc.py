# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:57:37 2023

@author: Horseman
"""

import compressorFunc as comp
import numpy as np
import matplotlib.pyplot as plt


T1 = 300 # [K ]
P1 = 100 # [kPa]
#massFlux = 0.294
massFlux = np.linspace(0.0294, 0.7, 10) #[kg/s]
psi = 1.04  
eta_c = 0.9

omega = np.linspace(20000, 120000, 10)

comp.getCompressorPerformancePlot(T1, P1, massFlux, omega, psi, eta_c)




    


