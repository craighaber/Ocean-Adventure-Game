#urchin.py
#Urchins are enemies that the player must avoid
#The urchin class is used to create urchin objects

import pygame
import os, sys
from random import *
pygame.init()

class urchin():
    """Creates an urchin, which the player must avoid"""
    def __init__(self,x,y,width,height,color):
        """Takes in the parameters of the urchin's x position, y position,
        width, height, color and creates many of the instance variables."""
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

        if self.color=='purple':
            self.img=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images',"urchpurp.png")).convert_alpha()

        elif self.color=='orange':
            self.img=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images',"urchoran.png")).convert_alpha()
            self.vel=randrange(5,16)

        elif self.color=='brown':
            self.vel=randrange(5,13)
            self.img=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images',"urchbrown.png")).convert_alpha()

        else: #green urchin 
            self.vel=4
            self.img=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images',"urchgreen.png")).convert_alpha()
            
    def draw(self,win):
        """Draws the urchin in the window and creates its hitbox.
        Takes in the parameter win, the window to draw the urchin in."""
        win.blit(pygame.transform.scale(self.img, (self.width,self.height)), (self.x,self.y))
        self.hitbox = (self.x+12,self.y+14,self.width-25,self.height-25)
              
    def collide(self,rect):
        """Checks if the urchin collides with any of the player's hitboxes.
        Takes in the parameter rect, which is one of the player's hitboxes.
        Returns True if there is a collision, otherwise returns false."""
    #checks if x coordinates of hitbox within eachother
        if rect[0]+rect[2]>self.hitbox[0] and rect[0]<self.hitbox[0]+self.hitbox[2]:
            #checks if y coordinates within eachother
            if rect[1] + rect[3] > self.hitbox[1] and rect[1]<self.hitbox[1]+self.hitbox[3]:
                return True
        return False
        
