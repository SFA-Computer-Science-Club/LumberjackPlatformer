# Main python file for the game
# Started 10/5/2022
# Simple mario-style platform game
# Add whatever you want I just put some comments
# Note on assets, use 16x16 for blocks (grass, brick, whatever), characters can be anything*

#Init some needed libraries
#Make sure pygame 2+ is installed! Very important
from csv import reader
import pygame
import classes
import os
import subprocess
import levels
import constants
from MainMenu.credits import *
import utilities
from assets.levels import levelOneMap


#Some values that may be needed globally
#Auto screen resolution
SCREEN_WIDTH = 0 #Might make this automatically update per screen size but manual for now
SCREEN_HEIGHT = 0
currentWorkDirectory = os.getcwd()
if os.name == "posix":
    #Linux
    output = subprocess.Popen("xrandr  | grep '\*' | cut -d' ' -f4", shell=True, stdout=subprocess.PIPE).communicate()[0] # Returns (WxH)
    stringSize = str(output, 'utf-8').split('x')
    SCREEN_WIDTH = int(stringSize[0])
    SCREEN_HEIGHT = int(stringSize[1])
else:
    print(os.name)
SCREEN_NAME = "SFA-Platformer 0.1a"
clock = pygame.time.Clock()
debugMode = True #Leave TRUE for development
inputMode = "keyboard" #Change to joystick for PRODUCTION

chosenMode = "none"
loaded = False

#Looping main screen music
pygame.mixer.init()
pygame.mixer.music.load('Platformer_Main_Menu_Song.mp3')
pygame.mixer.music.play(-1)


def main():
    global loaded
    global chosenMode
    mapLevel = None
    pygame.init()
    mainscreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.toggle_fullscreen()
    pygame.display.set_caption(SCREEN_NAME)
    player = classes.Player()
    player.setHealth(20)
    utilities.createLog()
    utilities.writeLog("Application starting")

    background = pygame.Surface(mainscreen.get_size())
    background = background.convert()
    background.fill(constants.WHITE)
    levelClass = levels.levels(mainscreen,currentWorkDirectory,SCREEN_WIDTH, SCREEN_HEIGHT)
    creditClass = credits(mainscreen, 5)

    if inputMode == "keyboard":
        utilities.writeLog("Starting keyboard mode")
    elif inputMode == "joystick":
        utilities.writeLog("Starting joystick mode")
    else:
        utilities.writeLog("No input type selected, shutting down")
        return 1

    while True: #Main game loop
        for event in pygame.event.get(): #Loops through every event, can be keyboard or mouse input etc
            if event.type == pygame.QUIT:
                utilities.writeLog("Process ending, nominal shutdown")
                return 0
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.stop()
        if chosenMode == "none":
            #ask user to choose mode or pull up main screen or something
            chosenMode = "credits"
            utilities.writeLog("Level One mode chosen")
        elif chosenMode == "levelOne":
            levelClass.levelOne()
        elif chosenMode == "credits":
            creditClass.main_loop()

        clock.tick(60)
        #mainscreen.blit(background, (0,0))
        #pygame.draw.rect(background, NAVYBLUE, pygame.Rect(0,200,200,300))
        pygame.display.flip()

main()
