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
massFlux = np.linspace(0.0294, 0.6, 20) #[kg/s]
psi = 1.04  
eta_c = 0.9

omega = np.linspace(50000, 200000, 20)

#P3 = comp.calcP03(T1, P1, massFlux)


fig, ax = plt.subplots()
fig.suptitle('Diagrama de desempeño del compresor')


for w in omega:
    pressures_3 =[]
    for i in massFlux:
        pressures_3.append(comp.calcP03(T1, P1, i, psi, eta_c, w/60))
    ax.plot(massFlux, pressures_3, color='k', linewidth = 2)
ax.grid(color='k', linestyle=':', linewidth=1)
ax.set_ylabel('Relación de Presion P03/P01')
ax.set_xlabel('Fujo de masa [kg/s]')
plt.show()


# fig, ax = plt.subplots(figsize=(10, 8))
# fig.suptitle('Diagrama de desempeño del compresor sin w')


# for w in omega:
#     pressures_3 =[]
#     for i in massFlux:
#         pressures_3.append(comp.calcP03(T1, P1, i, psi, eta_c))
#     pressures_3 = np.array(pressures_3)
#     omega = 
#     ax.plot(massFlux, pressures_3, color='k', linewidth = 2)
#     input()
# ax.grid(color='k', linestyle=':', linewidth=1)
# plt.show()

pressures_3_d =[]
for i in massFlux:
    pressures_3_d.append(comp.calcP03(T1, P1, i, psi, eta_c, method='dixon'))


