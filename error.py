'''
Module for handling custom errors
Ashley Ingram
'''
import sys, datetime

class ResourceException(Exception):
    """Exception Generated when a file is missing"""
    def __init__(self, message):
        """__init__ constructor method
        @param self
        @param message The filename of the file that is missing, in string format
        @return None (Application Exit)
        @desc Displays an error to the user when a file is missing, and stores the name of the file, along with time and other relevant info in a text file (error.txt). Then quits the application"""
        print("An error occurred!")
        print("Missing file " + message)
        log = open('error.txt', 'a')
        dtime = datetime.datetime.now()
        timestamp = str(dtime.day) + "/" + str(dtime.month) + "/" + str(dtime.year) + " " + str(dtime.hour) + ":" + str(dtime.minute) + ":" + str(dtime.second)
        errstring = "[{0}]\tResourceException - The file {1} was missing\n".format(timestamp, message)
        log.write(errstring)
        log.close()
        sys.exit()
        
class CorruptHighScores(Exception):
    """Exception Generated when High-Score file has invalid characters"""
    def __init__(self):
        """__init__ constructor method
        @param self
        @return None (Application Exit)
        @desc Displays error to the user when the high-score file is invalid/contains invalid characters. Logs the error in the error file (error.txt), and exits the application"""
        print("An Error Occurred!")
        print("The High Score file is Corrupt")
        log = open('error.txt', 'a')
        dtime = datetime.datetime.now()
        timestamp = str(dtime.day) + "/" + str(dtime.month) + "/" + str(dtime.year) + " " + str(dtime.hour) + ":" + str(dtime.minute) + ":" + str(dtime.second)
        errstring = "[{0}]\tCorruptHighScore - The High-Score file contained letters or other invalid characters\n".format(timestamp)
        log.write(errstring)
        log.close()
        sys.exit()        
