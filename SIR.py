#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 04:23:15 2020

@author: zahrashah
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
##With vital dynamics

# Total population, N.
N = int(input("Enter total nunber of population: "))
# Initial number of infected and recovered individuals, I0 and R0.
I0 = int(input("Enter the number of infected indiviuals at time 0: "))
R0 = 0
S0 = N - I0 - R0

# Contact rate, b, and mean recovery rate, k, (in 1/days).
B = float(input("Enter infectious rate: "))
days= float(input("Enter average duration of infection in days: "))
k=1./days
# A grid of time points (in days)
time= int(input("Enter the number of days for the simulation: "))
t = np.linspace(0, time, time)

# The SIR model differential equations.
def deriv(y, t, N, B, k):
    S, I, R = y
    dSdt = -B * S * I / N 
    dIdt = B * S * I / N - (k * I)
    dRdt = (k * I) 
    return dSdt, dIdt, dRdt

# Initial vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
sol = odeint(deriv, y0, t, args=(N, B, k))

S, I, R = sol.T


# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure()
g = fig.add_subplot(1,1,1, facecolor='#dddddd', axisbelow=True)
g.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
g.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
g.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
g.set_xlabel('Time /days')
g.set_ylabel('Number (1000s)')
g.set_ylim(0)
g.grid(b=True, which='major', c='w', linewidth=2, linestyle='-')
legend = g.legend()


plt.show()
