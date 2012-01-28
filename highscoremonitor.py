'''
Static class to handle high-score file operations
Ashley Ingram
'''

import error
class HighScoreMonitor:
    
    @staticmethod
    def getHighScores():
        """getHighScores
        @param None
        @return list highscores An ordered list of the current high scores
        @exception CorruptHighScore Thrown when a value has invalid characters (and can't be converted to int)
        """
        file = open('highscores.txt', 'r')
        highscores = []
        try:
            for line in file:
                highscores.append(int(float(line))) #fix inconsistancies with types in python versions
            file.close()
        except:
            error.CorruptHighScores()
            
        return sorted(highscores)
    
    @staticmethod
    def newHighScore(value):
        """newHighScore
        @param value int The score the user obtained in the game
        @return bool newhighscore Whether the player got a new high score
        @desc Calculates whether the player got a new high score or not,
        and returns a bool to that effect. If the player has a new score, it
        calls a method to update the high-score file to reflect this"""
        highScores = HighScoreMonitor.getHighScores()
        highScores.sort()

        newhighscore = False
        #Its unnecessary to iterate through all the high scores. If the players score is greater than the lowest, then its a new high score, and should replace the lowest. Its position is determined through a sort
        if value > highScores[0]:
            highScores[0] = value
            newhighscore = True

        highScores.sort()
        #The player has a new high score. This should be written to the high-score file to keep the scores up to date
        HighScoreMonitor.writeToFile(highScores)
        return newhighscore

    @staticmethod
    def writeToFile(highScores):
        """writeToFile
        @param highScores list A list of high scores to be written into the text file
        @returns None
        @desc Writes a list of high scores to the file, making them the new high scores the game uses"""
        file = open('highscores.txt', 'w')
        for score in sorted(highScores):
            file.write(str(int(score)) + "\n") #int casting first stops it from being written as a different type in different versions of Python
        file.close()
        
