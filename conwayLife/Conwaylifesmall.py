#!/usr/bin/env python

import pygame, sys, time, random
from pygame.locals import *

PPW = 10 # Pixel Per Square Width

n = input("Proportion of living cells? (%) ")
x = input("Number of horizontal tiles? ")
y = input("Number of vertical tiles? ")

xPPW = x*PPW
yPPW = y*PPW

c = []
l = []
b = 0
for i in range(int(n*x*y/(PPW*PPW))):
    c.append((PPW*random.randrange(x), PPW*random.randrange(y)))

pygame.init()
playSurface = pygame.display.set_mode((xPPW, yPPW))
pygame.display.set_caption("gameoflife")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

def glider(p,q):
    return [(p, q+PPW), (p+PPW, q), (p+PPW, q-PPW), (p, q-PPW), (p-PPW, q-PPW)]

def wrap(coords):
    xcoord,ycoord = coords
    return ((xcoord + xPPW) % xPPW,
            (ycoord + yPPW) % yPPW)

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if event.type == MOUSEBUTTONDOWN:
        pygame.time.wait(10)        
        g = pygame.mouse.get_pos()
        p = PPW*int(g[0]/PPW)
        q = PPW*int(g[1]/PPW)
        l.extend(glider(p, q))

    for a in range(0, xPPW, PPW):
        ss = [(a-PPW, b+PPW), (a, b+PPW), (a+PPW, b+PPW),
              (a-PPW, b),                 (a+PPW, b),
              (a-PPW, b-PPW), (a, b-PPW), (a+PPW, b-PPW)]
        if False:
            s = []
            for xcoord,ycoord in ss:
                s.append(wrap(xcoord,ycoord))
        else:
            s = map(wrap,ss)
        if ((len(set(s) & set(c)) == 3) or
            ((a, b) in c and len(set(s) & set(c)) == 2)):
            l.append((a, b))
            pygame.draw.rect(playSurface,black,Rect(a, b, PPW, PPW))
        else:
            pygame.draw.rect(playSurface,white,Rect(a, b, PPW, PPW))

    if b == PPW*y-PPW:
        b = 0
        c = l
        l = []
        pygame.display.flip()
    else:
        b += PPW
