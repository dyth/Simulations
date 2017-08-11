#!/usr/bin/env python
"""simulation of traffic patterns along a straight road"""
import matplotlib.pyplot as plt
import numpy as np

distance = 1600

class car:
    """a car has a position and speed"""
    def __init__(self, speed):
        self.speed = speed
        self.position = [0, 0]

    def move(self):
        if self.position[0] > distance:
            self.position[0] = self.speed
        else:
            self.position[0] += self.speed

            
speed, stdev, samples = 50, 10, 1000
cars = [car(s) for s in np.random.normal(speed, stdev, samples)]

plt.ion()
while True:
    xs = [car.position[0] for car in cars]
    ys = [car.position[1] for car in cars]
    plt.plot(xs, ys, 'o')
    for car in cars:
        car.move()
    plt.axis([0, distance, -10, 10])
    plt.pause(0.001)
    plt.clf()


