#!/usr/bin/env python
"""simulation of traffic patterns along a straight road"""
import matplotlib.pyplot as plt
import numpy as np


# global variables
meanSpeed, stdev, samples, distance = 50, 10, 100, 16000


class car:
    """a car has a position and speed"""
    def __init__(self, initialX, speed, patience):
        self.speed2 = None
        self.position = [initialX, 0]
        self.patience = patience
        self.count = 0
        if (initialX/100 == initialX/100.0):
            self.colour = 'r'
            self.speed = meanSpeed
        else:
            self.colour = 'b'
            self.speed = speed

    def move(self, cars):
        'move a car forwards'
        # speed reflects the inherent speed the driver wants to travel at
        # a driver may be impeded by another, thus enforcing a slower speed2
        if self.speed2 != None:
            self.count += 1
            if self.position[0] > distance:
                self.position[0] = self.speed2
            else:
                self.position[0] += self.speed2
        else:
            if self.position[0] > distance:
                self.position[0] = self.speed
            else:
                self.position[0] += self.speed
        # patience represents how many steps the driver can tolerate at a slower
        # speed. Once count reaches patience, the driver overtakes
        if self.count == self.patience:
            self.count = 0
            self.speed2 = None
            self.position[0] += 100
        # if there is a car of distance 10 away, adopt its speed
        # otherwise, use original speed
        for car in cars:
            if ((car.position[0] != self.position[0])
                and (car.position[0] - self.position[0] < 10.0)
                and (car.position[0] - self.position[0] > 0.0)
                and (car.position[1] == self.position[1])):
                if car.speed2 != None:
                    self.speed2 = car.speed2
                else:
                    self.speed2 = car.speed
                    return
            else:
                self.speed2 = None
                self.count = 0


# initialise list of cars -- depends on speeds and patiences
speeds = np.random.normal(meanSpeed, stdev, samples)
patience = np.random.poisson(2, samples)
cars = [car(distance*i/samples, speeds[i], patience[i]) for i in range(samples)]

plt.ion()
while True:
    # plot all vehicles, if car then blue else red for bus
    plt.clf()
    xs = [car.position[0] for car in cars]
    ys = [car.position[1] for car in cars]
    colour = [car.colour for car in cars]
    plt.scatter(xs, ys, c=colour)
    plt.axis([0, distance, -10, 10])
    plt.pause(0.1)
    # move all cars
    for car in cars:
        car.move(cars)
