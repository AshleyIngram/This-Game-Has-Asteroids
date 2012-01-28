'''
This is the main loop for the game. It handles all of the other classes, the event queue, and general initialization
Ashley Ingram
'''
import pygame, menu, highscore, game, gameover

pygame.init()

#Create the screen, etc
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption("This is a game with Asteroids - Ashley Ingram")
background = pygame.Surface(screen.get_size()).convert()
background.fill((0,0,0))
clock = pygame.time.Clock()

#The first level is always the menu. Create an instance of it
level = "menu" #Controls which level is updated, and therefore currently displayed to the user. This is how there are seperate screens for the menu, game, highscore, gameover, etc. Also used to determine where control/movement logic goes
menu_i = menu.Menu.getInstance(screen, background)
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #break the loop and end the game
        if event.type == pygame.USEREVENT:
            #A custom made event which occurs when the game finishes. This calls the gameover method in the relevant class, and is thrown from within the Game class ('game.py')
            if event.name == "Game Over":
                level = "gameover"
                gameover.GameOver.gameOver(screen, event.score)
                game_i.endGame() #Reset the game state, so the user can play again if they so wish
        if event.type == pygame.KEYDOWN:
            #KEYDOWN events are used for movement of sprites, and general game navigation
            if (event.key == pygame.K_DOWN):
                if (level == "menu"):
                    menu_i.moveDown()
            if (event.key == pygame.K_UP):
                if (level == "menu"):
                    menu_i.moveUp()
            if (event.key == pygame.K_RETURN):
                if (level == "menu"):
                    level = menu_i.getArrowPos() #Set the level to whatever the player is currently hovering on the menu
                elif (level == "hiscore"):
                    level = "menu" #When enter is pressed on the highscores, go straight back to the menu
                elif (level == "gameover"):
                    level = "menu" #When the game has finished, go back to the menu when the user presses enter
            if (event.key == pygame.K_SPACE):
                if (level == "game"):
                    game_i = game.Game.getInstance(screen)#New class instances don't iterate/get recreated endlessly because they make use of the singleton design pattern
                    game_i.movePlayerUp()
        if event.type == pygame.KEYUP:
            #More movement logic, to drop the player down when the space key isn't pressed
            if (event.key == pygame.K_SPACE):
                if (level == "game"):
                    game_i = game.Game.getInstance(screen)
                    game_i.movePlayerDown()
            if (event.key == pygame.K_ESCAPE):
                if (level == "game"):
                    level = "menu"
                    game_i.endGame()
                    

    #Depending on what level should be shown, update a different class and therefore show the user that screen
    if level == "menu":
        menu_i.update()
    elif level == "hiscore":
        highscore_i = highscore.HighScore.getInstance(screen)
        highscore_i.update()
    elif level == "game":
        game_i = game.Game.getInstance(screen)
        game_i.update()
    elif level == "gameover":
        gameover.GameOver.update()
    elif level == "quit":
        running = False #break the loop and end the game

    pygame.display.flip()
