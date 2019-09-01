#player.py
#The player class is used to create the "turtle" object in oceanAdventure.py
#The turtle is the character that the user controls

import pygame
import os, sys
from random import *
pygame.init()

class player():
    """Creates the turtle, the character the user controls."""
    def __init__(self,x,y,width,height):
        """Takes in the parameters of the player's x position, y postion,
        width, height, and creates many of the instance variables
        in the player class"""
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        #self.vel is the ammount of space the turtle moves on the screen
        #each time an arrow key is pressed
        self.vel=15
        #self.swimCount keeps track of which turtle image should be displayed on the screen
        self.swimCount=0
        swimList=[]
        for x in range(1,7):
                #append all the images of the turtle into swimList
                swimList.append((pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images','tur'+str(x)+'.png'))).convert_alpha())
        self.swimList=swimList
       
     
    def draw(self,win):
        """Draws the turtle in the window and creates its hitboxes.
            Takes in the parameter win, which is the window the turtle
            is drawn on."""
        if self.swimCount + 1>= 18:
            #reset swimCount so the turtle keeps swimming
            self.swimCount=0
        #add the next turtle image to the window every third frame
        win.blit(pygame.transform.scale(self.swimList[self.swimCount//3],(self.width,self.height)), (self.x,self.y))
        self.swimCount=self.swimCount+1
        
        #create the hitboxes for the shell,head, and arms
        self.shellhitbox = (self.x+2,self.y+24,self.width-30,self.height-47)
        self.headhitbox = (self.x+75,self.y+40,23,20)
        self.armshitbox = (self.x+60,self.y+12,10,self.height-22)
