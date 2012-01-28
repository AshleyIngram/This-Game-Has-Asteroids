'''
This class loads and scrolls the background of the game
Ashley Ingram
'''

import pygame, error

class GameBackground(pygame.sprite.Sprite):
	def __init__(self, screen):
                """__init__ constructor method
                @param self
                @param screen The surface to render the sprites on
                @return None
                @desc Loads the sprite required for the background, and renders it on screen
                @exception ResourceException This is thrown when the image can't be found"""
                self.screen = screen
                try:
                        self.image = pygame.image.load("sprites/game_bg.png").convert()
                except:
                        error.ResourceException("sprites/game_bg.png")

                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0
	
	def update(self):
                """update method
                @param self
                @return None
                @desc Scrolls the background of the screen by moving the sprite,
                and pushes it to the start when necessary to loop
                """
                self.rect.x -= 7
                if self.rect.x < -(530):
                        self.rect.x = 0
