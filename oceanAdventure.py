#Craig Haber 
#5/16/18

#*Note* This game requires the pygame module to play
#To install pygame, just type pip install pygame in the command prompt/ terminal
#The version of pygame used to make this game was 1.9.4,
#so it is possible it may not be compatible with newer versions of pygame

#This program makes 'Ocean Adventure', an endless video game
#Sea urchins randomly appear on the screen
#The user controls a turtle and loses if it collides with the sea urchins
#The turtle can be moved with the arrow keys
#Score is determined by how many seconds the player is alive
#As the game progresses, more urchins appear on the screen, and eventually they move faster

#The music is not ours and is from this video: https://www.youtube.com/watch?v=-hQt3LTGWxM

import pygame
import os, sys
from random import *
from game import *
pygame.init()

def main():
    #loads the music
    music_path = os.path.dirname(os.path.realpath(__file__)) + "\music.mp3"
    pygame.mixer.music.load(music_path);
    #sets music to an infite loop
    pygame.mixer.music.play(-1)
    #create an instance of the game class  
    game1=game()
    #create an instance of the player class at x=50 y=50 width=100 height=100
    turtle=player(50,50,100,100)
    #create an empty list to store urchin objects
    urchins=[]
    #totalloopiterations keeps track of the total number of iterations of the while loop
    totalloopiterations=0

    #game1.run is True unless the user quits
    while game1.run:

        #updates the screen
        game1.redrawWindow(turtle,urchins)

        bgSpeed=game1.bgMover()

        #moves the urchins in the list at the rate of their respective velocities
        game1.urchVelModulator(urchins)

        #returns the new list of urchins with the old ones removed
        urchins=game1.urchRemover(urchins)
           
        game1.fpsModulator()

        #for each urchin object that is onscreen
        
        for urch in urchins:
            #if it collides with any of the turtle hitboxes
            if urch.collide(turtle.shellhitbox) or urch.collide(turtle.headhitbox) or urch.collide(turtle.armshitbox):
                #display the endgame screen and reset the urchinitializervalue and totalloopiterations
                totalloopiterations=game1.endScreen(turtle,urchins)

        #add 1 for each iteration of the while loop
        totalloopiterations+=1
        game1.urchinitializer+=1

        #to resolve the error of self.urchinitialzier sometime being stuck above self.urchinitializer value
        if game1.urchinitializer>game1.urchinitializervalue:
            game1.urchinitializer=0
        
        #if totalloopiterations is divisible by 850, meaning there were 850 loop iterations since the last level change
        #and if the game level is not 5, since 5 is an endless level
        if totalloopiterations%850==0 and game1.level!=5:
            #call urchRateModulater, which increases the game's level
            #and decreases the urchinitializervalue to accompany the new level
            game1.urchRateModulator()
           
           
        #each time there have been the same number of while loop iterations as urchinitializervalue
        if game1.urchinitializer==game1.urchinitializervalue:
            #add an urchin to the screen and reset urchinitializer
            game1.urchCreator(urchins)
           
        game1.bgAdjuster()

        game1.eventExecuter()  

        #move the turtle based on the user's input commands
        game1.playerMover(turtle)

main()
