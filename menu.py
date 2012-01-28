'''
class for displaying the menu, and controlling associated sprites/logic
Ashley Ingram
'''

import pygame
from class_sprite.arrow import Arrow

class Menu:

    __instance = None

    @staticmethod
    def getInstance(screen, background):
        """static getInstance
        @param args passed to constructor. See __init__()
        @return Menu instance
        @desc Static method to implement the singleton pattern on the menu class
        if the class has been instansiated, it returns the existing instance. If not it creates one
        Prevents the class from being instansiated twice
        """
        
        if Menu.__instance == None:
            Menu.__instance = Menu(screen, background)
        return Menu.__instance
        
    def __init__(self, screen, background):
        """__init__ constructor function
        @param self
        @param screen The surface object used to render sprites on
        @param background The background for the screen, used to clear the screen every frame before reloading sprites
        @return None
        @desc Constructor function runs when the class is instansiated. Loads the background, and stores all variables required in other methods in class scope
        @exception ResourceException Thrown when the image file cannot be found
        """
        try:
            self.bg_img = pygame.image.load('sprites/menu_bg.png').convert()
        except:
            error.ResourceException('sprites/menu_bg.png')
        self.screen = screen
        self.background = background
        self.arrow = Arrow(screen)
        self.arrowGroup = pygame.sprite.Group(self.arrow)

    def getArrowPos(self):
        """getArrowPos
        @param self
        @return string The plaintext position of the arrow in relation to menu items ('game', 'hiscore', 'quit')
        @desc A method to get where the arrow is pointing, and return the plaintext representation of what level the user wants
        """
        if (self.arrow.index == 0):
            return "game"
        elif (self.arrow.index == 1):
            return "hiscore"
        elif (self.arrow.index == 2):
            return "quit"

    def moveUp(self):
        """moveUp
        @param self
        @return None
        @desc Abstraction method. Calls the arrow sprite instances moveUp method. This allows the main loop to interact solely with level instances, rather than managing the levels sprites too
        """
        self.arrow.moveUp()

    def moveDown(self):
        """moveDown
`       @param self
        @return None
        @desc Abstraction method. Calls the arrow sprite instances moveDown method. This allows the main loop to interact exclusively with level instances, as opposed to management of each levels sprites too
        """
        self.arrow.moveDown()

    def update(self):
        """update
        @param self
        @return None
        @desc Updates the screen and blits all menu-related sprites/objects
        """
        self.arrowGroup.clear(self.screen, self.background)
        self.arrowGroup.update()
        self.arrowGroup.draw(self.screen)
        self.screen.blit(self.bg_img, (0,0))
        self.screen.blit(self.arrow.image,(self.arrow.rect.x, self.arrow.rect.y))
