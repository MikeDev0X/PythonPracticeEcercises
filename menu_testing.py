from pygame import *
import sys

init()
screen=display.set_mode((800,600))
backgd=image.load()
while True:
    screen.fill((0,255,150))
    for i in event.get():
        if i.type==QUIT: sys.exit()
    display.flip()