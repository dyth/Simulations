#! usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *
n = input("Number of living cells? ")
cells = []
ground = []
for i in range(n):
    cells.append([10*random.randrange(100), 10*random.randrange(64)])
for x in range(100):
    for y in range (64):
        ground.append([10*x,10*y])

pygame.init()
playSurface = pygame.display.set_mode((1000, 640))
pygame.display.set_caption("gameoflife")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# 3 neighbours = born
# 3 or 2 neighbours = stays alive

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    playSurface.fill(white)
    livingcells = []
    for cell in cells:
        count = 0
        pygame.draw.rect(playSurface,black,Rect(cell[0],cell[1], 10, 10))
        if [cell[0]+10, cell[1]] in cells:
            count += 1
        if [cell[0]-10, cell[1]] in cells:
            count += 1
        if [cell[0], cell[1]+10] in cells:
            count += 1
        if [cell[0], cell[1]-10] in cells:
            count += 1
        if count == 2 or count == 3:
            livingcells.append([cell[0],cell[1]])
#    deadcells = []
    for element in ground:
        number = 0
        if [element[0]+10, element[1]] in cells:
            number += 1
        if [element[0]-10, element[1]] in cells:
            number += 1
        if [element[0], element[1]+10] in cells:
            number += 1
        if [element[0], element[1]-10] in cells:
            number += 1
        if number == 3:
            livingcells.append([element[0],element[1]])
        cells = livingcells
        
    pygame.display.flip()
    pygame.time.Clock().tick(10)
