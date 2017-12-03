#!/usr/bin/env python
"""construct distirbutions of personality from preference"""
from scipy.stats import norm
from sklearn.preprocessing import normalize
from numpy import dot


class Person:
    'a person has preference and strength. Assume normally distributed'
    def __init__(self, size):
        self.DISTRIBUTION = norm(0.0, 1.0)
        self.preference = normalize(distribution.rvs(size))
        self.children = []

    def find_affinity(otherPerson):
        'dot product of preferences is '
        return dot(self.preference, otherPerson.preference)
        


def create_population(size, abilities):
    'return random gaussian of preferences'
    return = [Person(size, abilities) for _ in range(size)]


def list_to_tree(population):
    'list to tree'
    for person in population:
        for otherPerson in population:
            person.find_affinity(otherPerson)


if __name__ == "__init__":
    size, abilities = 1000, 1
    population = create_population(size)
