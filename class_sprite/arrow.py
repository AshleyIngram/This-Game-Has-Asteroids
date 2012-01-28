'''
Class for controlling the arrow that appears on the menu.
Ashley Ingram
'''
import pygame, error

class Arrow(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        """__init__ constructor function
        @param self
        @param screen The surface to render sprites on
        @return None
        @desc Runs when the arrow is created. Loads the arrow image, and defines where it can/can't go
        @exception ResourceException Thrown when the sprite file doesnt exist"""
        super(Arrow, self).__init__()
        try:
            self.image = pygame.image.load('sprites/arrow.png').convert_alpha()
        except:
            error.ResourceException('sprites/arrow.png')
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.positions = [150, 200, 250] #A fixed array of the Y co-ords that the text is at. This can change if you modify the background image
        self.index = 0
        self.rect.y = self.positions[0]

    
    def moveUp(self):
        """moveUp method
        @param self
        @return None
        @desc Moves the arrow up to the next menu item"""
        if (self.index > 0):
            self.rect.y = self.positions[self.index - 1] #Decrease the array index to get the next lowest value - moving the arrow up
            self.index -= 1

    def moveDown(self):
        """moveDown method
        @param self
        @return None
        @desc Moves the arrow down to the next menu item"""
        if (self.index < len(self.positions) - 1):
            self.rect.y = self.positions[self.index + 1] #Opposite of above. Get the next highest array index and set it as the Y to make the arrow go down
            self.index += 1
