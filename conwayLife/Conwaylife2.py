#! usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *
n = input("Number of living cells? ")
x = input("Number of horizontal tiles? ")
y = input("Number of vertical tiles? ")
cells = []
ground = []
for i in range(n):
    cells.append([10*random.randrange(x), 10*random.randrange(y)])
# for a in range(x):
#     for b in range (y):
#         ground.append([10*a,10*b])

pygame.init()
playSurface = pygame.display.set_mode((10*x,10*y))
pygame.display.set_caption("gameoflife")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    playSurface.fill(white)
    livingcells = []
    for cell in cells:
        pygame.draw.rect(playSurface,black,Rect(cell[0],cell[1], 10, 10))
    for a in range(x):
        for b in range (y):
            number = 0
            if [10*a+10, 10*b] in cells:
                number += 1
            if [10*a-10, 10*b] in cells:
                number += 1
            if [10*a, 10*b+10] in cells:
                number += 1
            if [10*a, 10*b-10] in cells:
                number += 1
            
#    for element in ground:
#        number = 0
#        if [element[0]+10, element[1]] in cells:
 #           number += 1
  #      if [element[0]-10, element[1]] in cells:
   #         number += 1
    #    if [element[0], element[1]+10] in cells:
     #       number += 1
      #  if [element[0], element[1]-10] in cells:
       #     number += 1
            if number == 3 or (number == 2 and [10*a, 10*b] in cells):
                livingcells.append([10*a, 10*b])
    cells = livingcells
    pygame.display.flip()
    pygame.time.Clock().tick(10)
