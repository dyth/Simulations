#! usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *
n = input("Proportion of living cells? (%) ")
x = input("Number of horizontal tiles? ")
y = input("Number of vertical tiles? ")
cells = livingcells = []
b = 0
for i in range(int(n*x*y/100)):
    cells.append([10*random.randrange(x), 10*random.randrange(y)])

pygame.init()
playSurface = pygame.display.set_mode((10*x,10*y))
pygame.display.set_caption("gameoflife")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255,0,0)

while True:
    pygame.draw.rect(playSurface,red,Rect(0,0, 10, 10))
    pygame.draw.rect(playSurface,red,Rect(10*(x-1),10*(y-1), 10, 10))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if event.type == MOUSEBUTTONDOWN:
        pygame.time.wait(10)        
        g = pygame.mouse.get_pos()
        gx = 10*int(g[0]/10)
        gy = 10*int(g[1]/10)
        livingcells.extend([[gx,gy+10] , [gx+10,gy] , [gx+10,gy-10] , [gx,gy-10] , [gx-10,gy-10]])
    for a in range(x):
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
    if b == y:
        b = 0
        cells = livingcells
        livingcells = []
        pygame.display.flip()
    else:
        b += 1
