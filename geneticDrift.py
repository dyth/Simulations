#!/usr/bin/env python
"""How does changing the genotype affect phenoty[e expression?"""
import random

genomeLength = 10
bases = ['a', 't', 'c', 'g']
basePairs = {
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}


def createBase(length):
    'create random string consisting of a, t, c and g of length length'
    genome = ''
    for _ in range(length):
        genome += bases[random.randrange(0, 4)]
    return genome


def complement(genome):
    'create string which complements genome according to basePairs'
    return [basePairs[g] for g in genome]


def transcription(genome):
    'genome replication'
    comp = complement(genome)
    return comp, complement(comp)


genome = createBase(genomeLength)
print complement(genome)
print transcription(genome)
