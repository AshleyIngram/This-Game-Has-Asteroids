'''
The Reward class extends the pygame sprite class, and handles the logic and visual representation
of the reward/bonus the player aims to get throughout the game to supplement their score
Ashley Ingram
'''

import pygame, error, random

class Reward(pygame.sprite.Sprite):
    
    def __init__(self, screen, group, asteroidGroup):
        """__init__ constructor method
        @param self
        @param screen The surface for rendering sprites
        @param group The group the rewards are in, to prevent collisions
        @param asteroidGroup The group with asteroids in, to prevent collisions
        @return None
        @desc The constructor method assigns variables in class scope and loads images as relevant
        @exception ResourceException Throws when the image cannot be found"""
        super(Reward, self).__init__()
        self.screen = screen
        self.group = group
        self.asteroidGroup = asteroidGroup
        try:
            self.image = pygame.image.load('sprites/reward.png').convert_alpha()
        except:
            error.ResourceException('sprites/reward.png')
        self.rect = self.image.get_rect()
        self.getSpawnLocation()
        self.speed = 7

    def update(self, playerGroup, asteroidGroup):
        """update Method
        @param self
        @param playerGroup The current position of the player, used for collision
        @param asteroidGroup The current position of the asteroids, used for collision
        @return bool If the player obtains the reward, it returns true. If the reward goes off the screen without the player successfully obtaining it, it returns false
        @desc The update method moves the reward across the screen, and ensures it isn't colliding with anything
        """
        self.rect.x -= self.speed
        if (self.rect.x < 0 - self.rect.width):
            return False
        if pygame.sprite.spritecollideany(self, playerGroup):
            return True
        if pygame.sprite.spritecollideany(self,asteroidGroup):
            self.getSpawnLocation()
        

    def getSpawnLocation(self):
        """getSpawnLocation method
        @param self
        @return None
        @desc Finds a place to spawn the reward where it isn't colliding with itself or an asteroid"""
        #Spawn it off the screen, at a varying x and y co-ordinate
        self.rect.x = random.randint(self.screen.get_width() + 1, self.screen.get_width() * 2)
        self.rect.y = random.randint(0, self.screen.get_height() - self.rect.height)
        #Check if its colliding with another reward. If it is, check that that sprite isn't itself. This is necessary otherwise it'll always be colliding with something in the same group
        collision = pygame.sprite.spritecollide(self, self.group, False)
        #If the sprite collides with another reward or an asteroid, recursively call the function until it finds a place where it can spawn
        for col in collision:
            if (col != self):
                self.getSpawnLocation()
        collision = pygame.sprite.spritecollideany(self, self.asteroidGroup)
        if (collision):
            self.getSpawnLocation()
