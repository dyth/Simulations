#!/usr/bin/env python
"""neuron model with diffusion, fire at threshold: 100.0"""
import matplotlib.pyplot as plt
import thread, time, random

diffusionRate = 0.01
out, in1, in2 = [], [], []

def diffusion(outside, inside):
    'diffusion between the outside and all the inside values'
    sumInside = diffusionRate * sum(inside)
    newOut = sumInside + (1.0 - float(len(inside)) * diffusionRate) * outside
    factor = (outside - newOut) / sum(inside)
    for i in range(len(inside)):
        inside[i] += inside[i] * factor
    print newOut, inside
    return newOut, inside

def cycle(O, I):
    'go through one time step'
    while (I[0] < (sum(I) + O - 1.0)/float(len(I) + 1)):
        out.append(O)
        in1.append(I[0])
        in2.append(I[1])
        O, I = diffusion(O, I)

def initialiseNeurons(neurons):
    'start all neurons'
    inside = []
    for i in range(neurons):
        inside.append(1.0)
    return inside


neurons = 2
O, I = 300.0, initialiseNeurons(neurons)
cycle(O, I)

plt.plot(out)
plt.plot(in1)
plt.plot(in2)
print in1
plt.show()
