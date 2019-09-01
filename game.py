#game.py
#The game class is used to create "game1" in oceanAdventure.py
#This class contains several methods that allow the game to run

import pygame
import os, sys
from random import *
from urchin import *
from player import *
pygame.init()



class game():
    """The game class holds several methods that allow Ocean Adventure to run."""
    def __init__(self):
        """Creates many of the instance variables in the game class."""
        self.run=True
        #swidth/sheight are the width and height of the window
        self.swidth=1000
        self.sheight=750
        #create the window under the name self.win
        self.win = pygame.display.set_mode((self.swidth,self.sheight))
        pygame.display.set_caption("Ocean Adventure")
        #loads the background under the name self.bg
        #.convert_alpha() makes the image the desired pixel format to reduce lag
        self.bg = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images','bg.png')).convert_alpha()
        #self.bgX is the furthest left X coordinate of the background 
        self.bgX=0
        #self.bgX2 is the furtherest right X coordinate of the background
        self.bgX2 = self.bg.get_width()
        #self.clock initializes a pygame style clock
        self.clock = pygame.time.Clock()
        #self.speed is the maximum frames per second of the game
        self.speed=18
        #self.score represents the user's points
        self.score=0
        #self.level is the level of the game, which increases as the game goes on and caps at 5
        self.level=1
        #self.bgSpeed is how fast the background is scrolling
        self.bgSpeed=2.5
        
        #self.urchinitializer keeps track of the number of while loop iterations
        #when it equals urchinitializervalue in the main while loop, an urchin is created and it is set back to 0
        self.urchinitializer=0
        
        #self.urchinitializervalue is the number of while loop iterations until an urchin is created
        #this number decreases as the level increases
        self.urchinitializervalue=21
        
        #Creates USEREVENT+1, which happens every 3 seconds
        #It will result in an increase in score in the eventExecuter() function
        pygame.time.set_timer(pygame.USEREVENT+1,3000) 
        

    def redrawWindow(self,player,urchlist):
        """Redraws the game window, including the player, background, urchins, score,
        and level.
        Takes in an instance of the player class and a list of instances of
        the urchin classes as parameters."""

        #draw the background
        self.win.blit(self.bg, (self.bgX, 0))
        self.win.blit(self.bg, (self.bgX2, 0))
        #draw the player/urchins
        player.draw(self.win)
        for urch in urchlist:
            urch.draw(self.win)
        
        font = pygame.font.SysFont('comicsans', 30)
        scoreText = font.render('Score: ' + str(self.score),1, (255,255,255))
        levelText = font.render('Level: ' + str(self.level),1, (255,255,255))
        
        #add the the level/score score to the screen
        self.win.blit(scoreText, (900,10))
        self.win.blit(levelText, (800,10))
        
        #update the screen to draw new objects
        pygame.display.update()

    def bgMover(self):
        """Moves the background at a different rate depending on the level.
        The higher the background, the higher the rate.
        Returns the bgSpeed to main."""
        if self.level==1:
            self.bgSpeed = 2.5
        elif self.level==2:
            self.bgSpeed = 3.5
        elif self.level==3:
            self.bgSpeed = 4.5
        elif self.level==4:
            self.bgSpeed = 5.5
        elif self.level==5:
            self.bgSpeed = 6.5
        #moves the leftmost and rightmost parts of the background to
        #the right by the value of bgSpeed 
        self.bgX -= self.bgSpeed
        self.bgX2 -= self.bgSpeed
        

    def urchVelModulator(self,urchlist):
        """Determines the velocity of the urchlist based on the level
        and moves the urchins in the following directions:
        purple and orange urchins move to left,brown urchins move up,
        and green urchins move down.
        Purple urchins always move at the speed of the background.
        Takes in the list of instances of the urchin class as a parameter."""

        #loops through the list of instances of the urchin classes
        #purple urchins always move at bgSpeed
        for urch in urchlist:
            #if the level is 4 move all urchins except purple by an additional 3
            if self.level==4:
                if urch.color=="purple":
                    urch.x -= self.bgSpeed
                elif urch.color=="brown":
                    urch.y-=(urch.vel+ 3)
                elif urch.color=="green":
                    urch.y+=(urch.vel+ 3)
                else:
                    urch.x-= (urch.vel+ 3)
            #if the level is 5 move all urchins except purple by an additional 6
            elif self.level==4:
                if urch.color=="purple":
                    urch.x -= self.bgSpeed
                elif urch.color=="brown":
                    urch.y-=(urch.vel+ 6)
                elif urch.color=="green":
                    urch.y+=(urch.vel+ 6)
                else:
                    urch.x-= (urch.vel+ 6)
            #if the level is 1, 2, or 3, move the urchins only at their default velocity 
            else:
                if urch.color=="purple":
                    urch.x -= self.bgSpeed
                elif urch.color=="brown":
                    urch.y-=(urch.vel)
                elif urch.color=="green":
                    urch.y+=(urch.vel)
                else:
                    urch.x-= (urch.vel)

    def urchRemover(self,urchlist):
        """Removes urchins from the list of urchins when they move offscreen.
        Takes in the list of instances of the urchin classes as a parameter."""
        for urch in urchlist:
             if urch.x < 0-urch.width:
                 urchlist.pop(urchlist.index(urch))
        return urchlist

    def fpsModulator(self):
        """Computes how many milliseconds have passed since the previous call
        and makes sure the program is locked to a fps no greater than
        self.speed, which is 18."""
        self.clock.tick(self.speed)

    def urchRateModulator(self):
        """Changes the rate at which urchins appear on the screen
        depending on the level of the game, and increases the game level.
        This is called when the totalloopiterations is divisible by
        850 in the main while loop.
        self.urchinitializervalue is the number of while
        loop iterations it takes in the main function for a new urchin to be
        appended to the list of urchins."""
        
        self.level+=1
        
        if self.level==2:
            self.urchinitializervalue-=2
        elif self.level==3:
            self.urchinitializervalue-=3
        else: #level is 4 or 5
            self.urchinitializervalue-=4

            
    def urchCreator(self,urchlist):
        """Creates an urchin each time the urchinitializer is
        equal to self.urchinitializervalue in the main function.
        The type of urchin that will be created is random
        Sets self.urchinitiliazer to 0.""" 
        r = randrange(1,8)
        #1/8 chance a purple urchin is created
        if r==1:
            #appears randomly from y coordinates 0 to 590
            urchlist.append(urchin(1000,randrange(0,590),100,100,"purple"))
        #1/4 chance a brown urchin is created
        elif r==2 or r==3:
            #appears randomly from x coordinates 0 to 700
            urchlist.append(urchin(randrange(0,700),750,100,100,"brown"))
        #1/8 chance a green urchin is created
        elif r==4:
            #appears randomly from x coordinates 200 to 700
            urchlist.append(urchin(randrange(200,700),0,100,100,"green"))
        #1/2 chance orange urchin is created
        else:
            #appears randomly from y coordinates 0 to 590
             urchlist.append(urchin(1000,randrange(0,590),100,100,"orange"))
        #urchinitializer is set back to 0 and returned to main
        self.urchinitializer=0
        
    
    def bgAdjuster(self):
        """Moves the initial leftmost side or the intial rightmost side of the background
        to the rightmost part of the screen if it goes offscreen."""
        #if bgX offscreen
        if self.bgX < self.bg.get_width()*-1:
            #set bgX to the right side of the screen
            self.bgX =self.bg.get_width()
         #if bgX2 offscreen   
        elif self.bgX2 < self.bg.get_width()*-1:
            #set bgX2 to the right side of the screen
            self.bgX2 = self.bg.get_width()

    def eventExecuter(self):    
        """Checks if an event occured and executes it. The events
        are if the urser quits the game or if the score increases."""
        #makes a list of every event
        for event in pygame.event.get():
            #if the mouse is clicked on the upper right x button
            if event.type==pygame.QUIT:
                #quit the game
                self.run=False
                pygame.quit()
                quit()
            #if 3 seconds pass
            elif event.type==pygame.USEREVENT+1:
                #increase the user's score
                self.score+=1

        

    def playerMover(self,player):
        """Moves the player on the screen by player.vel based on user input
        from the arrow keys. Also prevents the player from moving offscreen
        Takes in an instance of the player class as a parameter."""
        #creates a list of all the keys that were pressed
        keys=pygame.key.get_pressed()
        #if the left arrow key is pressed and the player's x cord exceeds their vel 
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
        #if the right arrow key is pressed and the player's x coord
        #is less than the screen's width minus the width of the player
        if keys[pygame.K_RIGHT] and player.x <self.swidth-player.width:
            player.x += player.vel
        #if the up arrow key is pressed and the player's y coord exceeds their vel
        if keys[pygame.K_UP] and player.y > player.vel:
            player.y -= player.vel
        #if the down arrow key is pressed and the player's y coord is less
        #than the height of the screen minus 160 and minus their vel
        #160 is the approximate vertical length of the sand
        if keys[pygame.K_DOWN] and player.y < self.sheight - 160-player.vel:
            player.y += player.vel

    def highScoreCalculator(self):
        """Opens highScore.txt and determines if the current score is greater than
        the previous high score. If so, the current score becomes
        the high score. Returns the high score."""

        highScoreFile= os.path.dirname(os.path.realpath(__file__)) + "/highScore.txt"
        
        file = open(highScoreFile,'r')
        fileRead = file.readlines()
        HighScore = fileRead[0]
        #if the previous high score is less than the current score
        if int(HighScore) < self.score:
            file.close()
            #write current score in scores.txt
            fileWrite = open(highScoreFile, 'w')
            fileWrite.write(str(self.score))
            fileWrite.close()
            #return current score
            return self.score
        #otherwise return the high score
        return HighScore

    def endScreen(self,player,urchins):
        """Creates the screen when the player dies, displaying the current
        score and the high score. Takes in an instance of the player
        class and a list of urchins as parameters.
        Returns playerinitializervalue and totalloopiterations to be 21 and 0
        respectively."""
        
        run = True
        
        while run:
            #creates a list of the possible events
            for event in pygame.event.get():
                #if the user clicks the red x button
                if event.type == pygame.QUIT:
                    #quit the game
                    run = False
                    pygame.quit()
                    quit()
                #if the user clicks the screen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #exit the while loop and restart the game
                    run = False
            #set background to static bg
            self.win.blit(self.bg, (0,0))

            #Add text to the screen to display current score/high score/instructions
            largeFont = pygame.font.SysFont('comicsans', 80)
            highScore = largeFont.render('High Score: ' + str(self.highScoreCalculator()),1,(255,255,255))
            self.win.blit(highScore,(self.swidth/2 - highScore.get_width()/2,200))
            newScore = largeFont.render('Score: '+ str(self.score), 1, (255,255,255))
            self.win.blit(newScore,(self.swidth/2 - newScore.get_width()/2,300))
            smallFont = pygame.font.SysFont('comicsans', 40)
            clickScreen = smallFont.render('Click the screen to play again',1,(255,255,255))
            self.win.blit(clickScreen,(self.swidth/2-clickScreen.get_width()/2,550))

            pygame.display.update()
            
            #remove urchins as they try to appear on the screen
            for urch in urchins:
                urchins.remove(urch)

        #simulate a new game at level 1    
        self.level=1   
        player.x=50
        player.y=50
        self.score=0
        #return playerinitializervalue and totalloopiterations to be 21 and 0 respectively
        self.urchinitializervalue=21
        totalloopiterations=0
        return totalloopiterations
