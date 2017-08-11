#!/usr/bin/env python
"""stochastic zero-player financial model based on hyperpolarising neurons: fire at threshold: 100.0"""
import matplotlib.pyplot as plt
import random, math
import numpy as np

# number of different stocks
number = 100

def sigmoid(x):
    return np.arcsinh(float(x))

def index(x):
    'return new index of stock'
    return np.sinh(float(x))

def linkage(stocks):
    'return value of stocks after market response'
    number = len(stocks)
    coeff = [math.cos(2 * math.pi * i / number) for i in range(number)]
    newStocks = [0 for _ in range(number)]
    for x in range(number):
        for i in range(number):
            position = (x + i + number) % number
            #newStocks[position] += coeff[i] * stocks[x] / sum(stocks)
            newStocks[position] *= abs(stocks[position]) * coeff[i] * stocks[x] / (sum(stocks) * sum(stocks))
    return [stocks[i] + newStocks[i] for i in range(number)]

def trim(history):
    'if history > 50 (screen display), trim'
    if (len(history) == 200):
        history.pop(0)
    return history

def work(index):
    'increment index such that it increases'
    return index + random.randint(-1, 1)

def bust(index):
    'if below absorbing barrier, change stock value back to new random value'
    if (sigmoid(index) < 0):
        index = random.randint(0, 50)
    return index

plt.ion()

indexes = [random.randint(-50, 50) for _ in range(number)]
histories = [[sigmoid(i)] for i in indexes]

while True:
    values = linkage([sigmoid(work(i)) for i in indexes])
    [trim(histories[i]).append(values[i]) for i in range(number)]
    indexes = [bust(index(x)) for x in values]
    
    # plot and draw screen
    [plt.plot(h) for h in histories[20:]]
    plt.pause(0.001)
    plt.clf() # clear screen

