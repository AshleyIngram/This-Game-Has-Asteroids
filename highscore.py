'''
Class for displaying the high scores to the user, and controlling sprites required for this menu item/level
Ashley Ingram
'''

import pygame, error
from highscoremonitor import HighScoreMonitor

class HighScore:

    __instance = None

    @staticmethod
    def getInstance(screen):
        """static method getInstance
        @param screen Passed directly to constructor. See __init__()
        @return HighScore instance
        @desc Implements singleton design pattern, preventing 2 instances of the class existing. If an instance exists, it returns that. Otherwise it creates one"""
        if HighScore.__instance == None:
            HighScore.__instance = HighScore(screen)
        return HighScore.__instance

    def __init__(self, screen):
        """__init__ constructor method
        @param self
        @param screen The surface object to render sprites on
        @return None
        @desc Saves all relevant variables in class scope. Load the background file
        @exception ResourceException Thrown when an image file is missing """
        self.screen = screen
        try:
            self.bg = pygame.image.load('sprites/hiscore_bg.png').convert_alpha()
        except:
            error.ResourceException('sprites/hiscore_bg.png')
            
    def update(self):
        """update method
        @param self
        @return None
        @desc Updates the high score screen. Blits all relevant sprites and positions text. Updates the scores if they change"""
        highscores = HighScoreMonitor.getHighScores()
        i = 0 
        textGroup = []
        font = pygame.font.Font(None, 30)
        #Put all the high scores in a list.
        #Iterate through the list and output them.
        #Use a control variable to define which key the highscore is,
        #and then put it in a different place depending on what
        #high score position its in
        #This means all the high-scores appear in the right place and not in one blob
        for score in reversed(sorted(highscores)):
            text = font.render(str(score), True,(255,255,255), (0,0,0) )#text to be rendered, anti-aliasing, colour, bg-colour
            rect = text.get_rect()
            if i == 0:
                rect.x = 100
                rect.y = 117
            if i == 1:
                rect.x = 100
                rect.y = 170
            if i == 2:
                rect.x = 100
                rect.y = 230
            if i == 3:
                rect.x = 100
                rect.y = 280
            if i == 4:
                rect.x = 100
                rect.y = 330
            if i == 5:
                rect.x = 390
                rect.y = 117
            if i == 6:
                rect.x = 390
                rect.y = 170
            if i == 7:
                rect.x = 390
                rect.y = 230
            if i == 8:
                rect.x = 390
                rect.y = 280
            if i == 9:
                rect.x = 390
                rect.y = 330
            textGroup.append({'object':text,'rect':rect})
            i += 1
            
        self.screen.blit(self.bg, (0,0))
        for text in textGroup:
            self.screen.blit(text['object'], text['rect'])
