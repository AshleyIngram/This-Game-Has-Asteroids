'''
Static Class for handling the game over condition
Ashley Ingram
'''
import pygame, error
from highscoremonitor import HighScoreMonitor

class GameOver:

    screen = None
    score = None
    bg = None

    @staticmethod
    def gameOver(screen, score):
        """gameOver
        @param screen The screen sprites need to be rendered on
        @param score int The score the player obtained before dying
        @return None
        @desc Stores the relevant values as static properties, load the required background images
        @exception ResourceException Thrown when one of the images cant be loaded"""
        GameOver.screen = screen
        GameOver.score = score
        #Check if the score the user posted is a new high score. If it is then show a different screen for intuitivity/user-feedback purposes
        isHighScore = HighScoreMonitor.newHighScore(score)
        if (isHighScore):
            try:
                GameOver.bg = pygame.image.load('sprites/gameover_bg_hiscore.png').convert()
            except:
                error.ResourceException('sprites/gameover_bg_hiscore.png')
        else:
            try:
                GameOver.bg = pygame.image.load('sprites/gameover_bg.png').convert()
            except:
                error.ResourceException('sprites/gameover_bg.png')
    
    @staticmethod
    def update():
        """update
        @param None
        @return None
        @desc Update the background of the game over, therefore keeping the image displayed to the user
        """
        GameOver.screen.blit(GameOver.bg, (0,0))
