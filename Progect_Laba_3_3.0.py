import pygame
import random as rn
import numpy as np
from pygame.draw import*

pygame.init()
h0 = 500
w0 = 600
FPS = 30
screen = pygame.display.set_mode((h0,w0))

red = (255, 0, 0)
green = (0, 255, 0)
d_green = (0, 130, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
purple = (150, 30, 30)  #make thiscolor better

def apple(screen, x, y, r, color):
    circle(screen, color, (x, y), r)

def tree(screen, x, y, l, color_stvol, color_listia, levels):
    """
        x, y - coordinates of the center of the trunk from below
        l - tree trunk length
    """
    line(screen, color_stvol, (x, y), (x,y-l), l//4) #trunk

    ellipse(screen, color_listia, (x-l/2, y-l*1.6, l, 0.9*l), 0) #leaves
    ellipse(screen, yellow, (x-l/2-1, y-l*1.6-1, l+2, 0.9*l+2), 1)
    ellipse(screen, color_listia, (x-l, y-l*2.4, 2*l, 1.0*l), 0)
    ellipse(screen, yellow, (x-l-1, y-l*2.4-1, 2*l+2, 1.0*l+2), 1)
    ellipse(screen, color_listia, (x-l*0.6, y-3.4*l, 1.2*l, 1.6*l), 0)
    ellipse(screen, yellow, (x-l*0.6-1, y-3.4*l-1, 1.2*l+2, 1.6*l+2), 1)
                    

def sun_pro(screen, x, y, r):
    for i in range(r,1,-1):
        circle(screen, (150+r-i, 150+r-i,255-r+i), (x, y), i)
       
def apple_tree_common(screen, x, y, l, color_stvol, color_listia):
    """
        draw tree with apples
    """
    tree(screen, x, y, l, color_stvol, color_listia, 3)
    apple(screen, x+l/4, y-l, l/8, purple)
    apple(screen, x+l/2, y-1.9*l, l/8, purple)
    apple(screen, x-l/2, y-1.9*l, l/8, purple)
    apple(screen, x+l/4, y-l*3.0, l/8, purple)

def screen_color(screen):
    rect(screen, (150,150,255), (0, 0, h0, w0/2), 0)
    rect(screen, (50,255,100), (0, w0/2, h0, w0/2), 0)

def uni_eye(screen, x, y, r):
    """
        draw eye
        x,y -- coordinates of the center of the eye
    """
    circle(screen, purple, (x, y), r)
    ellipse(screen, white, (x-r/2, y-r/4, r, r/2), 0)
    circle(screen, black, (x+r/4, y), r/6)

def uni_tail(screen, x, y, l):
    """
        draw tail or mane
        l -- tail's length. If positive tail is left, if negative tail is right
        x,y -- coordinates of the beginning of the tail
        dx, dy -- random offset of the elements of the tail
    """
    for i in range(0,int(abs(l)),2):
        dx , dy = rn.randint(i//8, i//4)+abs(l)//4, abs(l)/50*(rn.randint(0,4)+2)
        ellipse(screen, (rn.randint(150,200), rn.randint(150,200), rn.randint(150,200)), (x-3*np.sign(l)*i**0.6+rn.randint(int(-2*i**0.5),int(2*i**0.5)), y-dy+i, np.sign(l)*1.5*dx, 2*dy))

def uni_body(screen, x, y, l):
    """
        draw unihorn's body
        l -- body's length. If positive unihorn is left, if negative unihorn is right
        x,y -- coordinates of the center of the body
    """
    ellipse(screen, white, (x-abs(l), y-abs(l/2), abs(2*l), abs(l*0.8)), 0)
    line(screen, white, (x-0.8*l, y), (x-0.8*l, y+abs(l*0.8)), abs(l)//10)
    line(screen, white, (x-0.3*l, y), (x-0.3*l, y+abs(l*0.7)), abs(l)//10)
    line(screen, white, (x+0.3*l, y), (x+0.3*l, y+abs(l*0.8)), abs(l)//10)
    line(screen, white, (x+0.8*l, y), (x+0.8*l, y+abs(l*0.7)), abs(l)//10)
    line(screen, white, (x+0.78*l, y), (x+0.78*l, y-abs(l*0.8)), abs(l)//3)
    polygon(screen, red, [(x+0.80*l+l*0.08, y-abs(l*0.90)), (x+0.90*l+l*0.09, y-abs(l*1.55)), (x+0.90*l+l*0.05, y-abs(l*0.90))])
    if l<0:
        ellipse(screen, white, (x+0.60*l-abs(0.5*l), y-abs(l*0.95), abs(0.5*l), abs(0.4*l)), 0)
        ellipse(screen, white, (x+0.90*l-abs(0.4*l), y-abs(l*0.82), abs(0.4*l), abs(0.2*l)), 0)
    else:
        ellipse(screen, white, (x+0.60*l, y-abs(l*0.95), abs(0.5*l), abs(0.4*l)), 0)
        ellipse(screen, white, (x+0.90*l, y-abs(l*0.82), abs(0.4*l), abs(0.2*l)), 0)

def unihorn(screen, x, y, l):
    """
        draw unihorn's body
        l -- body's length. If positive unihorn is left, if negative unihorn is right
        x,y -- coordinates of the center of the unihorn
    """
    uni_tail(screen, x-l, y-abs(l//10), l*0.7)
    uni_body(screen, x, y, l)
    uni_eye(screen, x+0.93*l, y-abs(l*0.78), abs(l*0.10))
    uni_tail(screen, x+0.60*l, y-abs(0.90*l), l*0.8)
    
        
screen_color(screen)
unihorn(screen, 240, 350, 60)
for i in range(15):
    apple_tree_common(screen, 150+rn.randint(-100,100), 300+i*20, 40+rn.randint(0,30), white, d_green) 
sun_pro(screen, h0-100, 100, 100)
unihorn(screen, 400, 450, 80)
unihorn(screen, 400, 300, -60)
unihorn(screen, 400, 550, -30)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

