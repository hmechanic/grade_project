#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:52:09 2023

@author: juda
"""

import numpy as np

########## DATOS DE ENTRADA ############

r1 = 24 # m
r2 = 30 # m
rho = 1 # kg/m^3
P1 = 101.325 # kPa
cp = 1 # J / kg K
T1 = 600 # K 
k = 1.4
empuje = 10 # N
LHV_methane = 50016 # kJ/kg
#----------------------------------------


#----------------------------------------------

phi = np.linspace(0.5, 1.7, 20)
phi = np.round(phi, 2)

massFlux = np.linspace(0.0294, 0.7, 20) #[kg/s]

#------------------------------------------

# Cámara de combustión

massFlux_com = np.matmul(massFlux.reshape(len(massFlux), 1), phi.reshape(1, len(massFlux)))
massFlux_com = massFlux_com/(2/0.21)

massFlux_total = np.zeros(massFlux_com.shape)
for row in range(len(massFlux)):
    massFlux_total[row,:] = massFlux_com[row,:] + massFlux[row]

h_prod = (massFlux_com/massFlux_total)*LHV_methane + h_comp

A1 = np.pi *r1**2
A2 = np.pi *(r1**2-r2**2)
A3 = A2
V1 = massFlux/(rho*A1) # Velocidad a la salida de la cámara de combustión
V2 = (r1**2 / (r1**2-r2**2))*V1 # Velocidad cambio de sección

h01 = cp*T1 + (V1**2)/2 
P2 = rho*(V1**2  )*(1 - (A1**2)/(A1**2)) + P1 # Bernoulli
T2 = (P1/P2)**((k-1)/k) * T1

P3 = empuje/A3
V3 = empuje/massFlux
T3 = (P2/P3)**((k-1)/k) * T2

h03 = cp*T3 + (V3**2)/2

w = h01 - h03

