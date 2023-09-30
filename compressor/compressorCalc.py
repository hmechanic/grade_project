# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 23:57:37 2023

@author: Horseman
"""

import compressorFunc as comp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


T1 = 300 # [K ]
P1 = 100 # [kPa]
#massFlux = 0.294
massFlux = np.linspace(0.0294, 0.7, 20) #[kg/s]
psi = 1.04  
eta_c = 0.9

omega = np.linspace(20000, 120000, 20)

#comp.getCompressorPerformancePlot(T1, P1, massFlux, omega, psi, eta_c)


    
com_power = comp.getCompressorPower(omega, massFlux, psi)

X, Y = np.meshgrid(omega, massFlux)

# Assuming you have defined com_power, X, and Y as in your code
# Create a custom colormap where red represents higher values and blue represents smaller ones
colors = cm.jet(np.linspace(0, 1, 256))  # You can choose a different colormap if desired
colors = colors[::-1]  # Reverse the colormap to make red higher and blue lower

# Create a colormap object from the custom colors
cmap = cm.colors.ListedColormap(colors)

# Create the 3D plot
ax = plt.figure().add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, com_power, cmap=cmap, linewidth=0)

# You can also add color bar for reference
cbar = plt.colorbar(surf)
cbar.set_label('Color Scale')

plt.show()

### Potencia entregada por el combustible

