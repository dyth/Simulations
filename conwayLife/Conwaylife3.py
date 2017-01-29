#! usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *
n = input("Proportion of living cells? (%) ")
x = input("Number of horizontal tiles? ")
y = input("Number of vertical tiles? ")
cells = []
for i in range(int(n*x*y/100)):
    cells.append([10*random.randrange(x), 10*random.randrange(y)])

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
#            elif pygame.mouse.get_pressed(button1) == true:
    if event.type == MOUSEBUTTONDOWN:
        print pygame.mouse.get_pos()

#    playSurface.fill(white)
    livingcells = []
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
            if [10*a+10, 10*b+10] in cells:
                number += 1
            if [10*a-10, 10*b+10] in cells:
                number += 1
            if [10*a-10, 10*b-10] in cells:
                number += 1
            if [10*a+10, 10*b-10] in cells:
                number += 1
            if number == 3 or (number == 2 and [10*a, 10*b] in cells):
                livingcells.append([10*a, 10*b])
                pygame.draw.rect(playSurface,black,Rect(10*a,10*b, 10, 10))
            else:
                pygame.draw.rect(playSurface,white,Rect(10*a,10*b, 10, 10))
    cells = livingcells
    pygame.display.flip()
    pygame.time.Clock().tick(10)
