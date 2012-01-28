'''
class for handling game logic and managing game related sprites
Ashley Ingram
'''

import pygame, error, math, random
from time import *
from class_sprite.player import Player
from class_sprite.asteroid import Asteroid
from class_sprite.reward import Reward
from class_sprite.gamebackground import GameBackground

class Game:

    __instance = None

    @staticmethod
    def getInstance(screen):
        """static getInstance
        @param screen Passed to constructor. See __init__()
        @return Game Instance
        @desc Implements the singleton design pattern.
        Only allows 1 instantation of the game class by returning the existing
        instance if one exists (and creating a new one if it doesnt).
        """
        if Game.__instance == None:
            Game.__instance = Game(screen)
        return Game.__instance
    
    def __init__(self,screen):
        """__init__ constructor method
        @param self
        @param screen The surface object to render sprites on
        @desc Ran when a new game object is created.
        Loads background and other required sprites
        Stores all relevant/required variables in class scope
        @exception ResourceException Thrown if the background image cannot be found
        """
        self.screen = screen
        self.bg = GameBackground(self.screen)
        self.player = Player(screen)
        asteroidGroup = pygame.sprite.Group()
        rewardGroup = pygame.sprite.Group()
        self.rewardBlit = False
        i = 3
        while (i > 0):
            #Create the 3 instances of the asteroid that exist throughout the game
            a = Asteroid(screen, asteroidGroup)
            asteroidGroup.add(a)
            i -= 1
        self.asteroidGroup = asteroidGroup
        self.rewardGroup = rewardGroup
        self.playerGroup = pygame.sprite.Group(self.player)
        #time the game in order to calculate the score
        self.time = time()
        self.score = 0
        self.rewards = 0
        self.multiplier = 1
        self.counter = random.randint(0, 750)

    def update(self):
        """update method
        @param self
        @return None
        @desc Update the game state, reload sprites, maintain game state,
        throw game over when completed, respawn sprites as necessary"""

        #Decrease the counter for quasi-random reward spawning
        self.counter -= 1

        if (self.counter == 0):
            #Create a new reward when the counter is 0, and reset the timer. This creates a semi-random, none predictable method of rewards spawning
            self.counter = random.randint(0, 750)
            self.rewardGroup.add(Reward(self.screen, self.rewardGroup, self.asteroidGroup))
        self.bg.update()
        state = self.player.update(self.asteroidGroup)
        if (state == "Game Over"):
            #Throw the game over event onto the event queue, to be handled in the main while loop
            event = pygame.event.Event(pygame.USEREVENT, {"name":"Game Over", "score":self.score})
            pygame.event.post(event)
        
        for asteroid in self.asteroidGroup:
            asteroid.update()
        for reward in self.rewardGroup:
            rewardObtained = reward.update(self.playerGroup, self.asteroidGroup)
            if rewardObtained == True:
                #Destroy the reward if the user has obtained it, and increase the multiplier. This leads to steady increase of player score when they collect multiple rewards in a row (without missing one)
                self.rewards += (20 * self.multiplier)
                self.multiplier += 1
                reward.kill()
                self.rewardBlit = 20
            else:
                #If the player has missed the reward, and its gone of the screen they should lose the multiplier they have already obtained
                self.multipler = 1
        #Update the display
        self.screen.blit(self.bg.image, (self.bg.rect.x,self.bg.rect.y))
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        for asteroid in self.asteroidGroup:
            self.screen.blit(asteroid.image, (asteroid.rect.x, asteroid.rect.y))
        for reward in self.rewardGroup:
            self.screen.blit(reward.image, (reward.rect.x, reward.rect.y))

        #Calculate the current score based on the time they've been playing, and the rewards they've collected
        self.score = math.floor(((time() - self.time) * 4) + self.rewards)

        #Display the current score to the user, so they know how they're doing
        font = pygame.font.Font(None, 20) 
        text = font.render(str(self.score), True, (255,255,255), (0,0,0))
        textrect = text.get_rect()
        self.screen.blit(text, textrect)

        #If the player has recently got a reward, display the amount of points they have
        if self.rewardBlit != False:
            font = pygame.font.Font(None, 20)
            text = font.render(("+" + str(20 * (self.multiplier - 1))), True, (255,255,255), (0,0,0))
            textrect = text.get_rect()
            textrect.x = self.player.rect.x
            textrect.y = self.player.rect.y - 20
            self.screen.blit(text, (textrect.x, textrect.y))
            self.rewardBlit -= 1 #When the player gets an award, rewardBlit is set to the amount of frames it should show for. This is decreased every frame here, triggering the end of the if statement (which executes every loop)
        
        
    def movePlayerUp(self):
        """movePlayerUp
        @param self
        @return None
        @desc Abstraction method to prevent main while loop from handling all sprites as well as levels. Moves the player up using the player sprite instance"""
        self.player.moveUp()

    def movePlayerDown(self):
        """movePlayerDown
        @param self
        @return None
        @desc Abstraction method to move the player down, so the main while loop doesn't have to handle all sprites individually. Passes to the moveDown method in player instance"""
        self.player.moveDown()

    def endGame(self):
        """endGame
        @param self
        @return None
        @desc Deletes the reference to the class in the singleton design pattern, so a new instance is created next time its requested.
        The current instance should be garbage collected as there are no remaining references to it
        This allows a new game to be started without the old state existing, meaning a new score, player position etc
        """
        Game.__instance = None
