import datetime
import os
import pygame

doLogging = True
currentWorkDirectory = os.getcwd()
pathToLogFolder = currentWorkDirectory + "/log/"
logFile = pathToLogFolder + str(datetime.date.today()) + "-" + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second) + ".txt"

def createLog():
    if doLogging == False:
        return
    logfile = open(logFile, "w")
    # logfile.write("Log Created\nPygame Version: {}\nPlatformer version: {}\nInputMode: {}\nDebugMode: {}\nCurrentDirectory: {}".format(pygame.version.ver, SCREEN_NAME, inputMode, debugMode, currentWorkDirectory)) #Writes some basic things upon creation
    logfile.close()

def writeLog(input):
    if doLogging == False:
        return
    logfile = open(logFile, "a")
    logfile.write("\n" + input) #Writes a new line given an input
    logfile.close()