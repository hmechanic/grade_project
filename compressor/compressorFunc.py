# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

#Datos geometricos del compresor
alpha1 = 32 # Grados
rh1 = 7.7E-3 # Radio del ojo del compresor a la entrada [m]
rs1 = 26.7E-3 # radio mas grande de los alaber a la entrada [m]
r2 = 34.175E-3 # radio a la salida [m]
Z = 16 # Número de alabes
beta2p = 0 # angúlo de salida del alabe: es el angulo medido respecto a la dirección radial
A1 = np.pi * rs1**2 # área de la entrada de la turbina
#psi = 1.04 # lis valores posibles para este factor


# Propiedades del aire
R = 0.287 # kJ/(kg K)
Cp = 1.005 # kJ/(kg K )
k = 1.4 # Coeficiente de dilatación adiabática

rho1 = 1.204 # Densidad del aire a la entrada [kg/m3]







def speedSound(T):
    a = (k*R*T*1000)**(1/2)
    
    return a 

def getSigma(U2, Cr2 = 0, method = 'stanitz'):
    
    degtorad= np.pi / 180
    phi2 = Cr2/U2
    if method == 'stodola':
        sigma = 1 - ((np.pi/Z)*np.cos(beta2p*degtorad)/(1 - phi2*np.tan(beta2p*degtorad)))
    if method == 'stanitz':
        sigma = 1 - 0.63*np.pi/Z
        
    return sigma

def getOmega(massFlux):
    degtorad= np.pi / 180
    num = massFlux/(np.pi*(rs1**2)*rho1)
    den = ((1/(np.cos(alpha1*degtorad))**2) - 1)**(1/2)
    omega = num/(den*rs1)
    return omega
    
def calcP03(T1, P1, massFlux, psi, eta_c, omega = None, method='saravanamutto'):
    
    Cx1 = massFlux/(rho1*A1)
    M1 = Cx1/speedSound(T1)
    if M1 >= 0.3: 
        pass
        
    if omega == None:
        omega = getOmega(massFlux)
    
    U2 = omega*r2
    sigma = getSigma(U2)
    T01 = T1 + (Cx1**2)/(2*Cp*1000)
    P01 = P1 * ((T01/T1)**(k/(k-1)))
    
    print('Mach: ', M1, '-->', 'T1 estancamiento' ,T01)
    Mu = U2/speedSound(T01)
    if method == 'saravanamutto':
        P03_P01 = (1 + (eta_c*psi*sigma*U2**2)/(Cp*T01*1000))**(k/(k-1))
    elif method == 'dixon':    
        P03_P01 = (1 + ((k-1)*(sigma/psi)*(Mu**2)))**(k/(k-1))
    #P03 = P03_P01*P01
    
    if omega == None:
        return P03_P01, omega
    else:
        return P03_P01

def getMassFlux(rpm):
    
    degtorad= np.pi / 180
    massFlux = rpm*rs1*((1/(np.cos(alpha1*degtorad))**2) -1)**(1/2) * (np.pi*(rs1**2-rh1**2)*rho1)
    
    return massFlux


    
    
def getCompressorPerformancePlot(T1, P1, massFlux, omega, psi, eta_c):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle(f'Diagrama de desempeño del compresor  \psi = {psi}')
    
    
    for w in omega:
        pressures_3 =[]
        for i in massFlux:
            pressures_3.append(calcP03(T1, P1, i, psi, eta_c, w*(np.pi*2/60)))
        line, = ax.plot(massFlux, pressures_3, color='k', linewidth = 1)
        ax.annotate(f'{int(w)} rpm', xy=(0.3, pressures_3[1]))
    ax.grid(color='k', linestyle=':', linewidth=1)
    ax.set_ylabel('Relación de Presion P03/P01')
    ax.set_xlabel('Fujo de Masa [kg/s]')
    plt.show()
    

    
    
    
    