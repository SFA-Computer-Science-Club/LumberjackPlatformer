# Main python file for the game
# Started 10/5/2022
# Simple mario-style platform game
# Add whatever you want I just put some comments
# Note on assets, use 16x16 for blocks (grass, brick, whatever), characters can be anything*

#Init some needed libraries
#Make sure pygame 2+ is installed! Very important
from csv import reader
import csv
import pygame
import classes
import os
import subprocess
import datetime
import random
from assets.levels import levelOneMap


#Some values that may be needed globally
#Auto screen resolution
SCREEN_WIDTH = 0 #Might make this automatically update per screen size but manual for now
SCREEN_HEIGHT = 0
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
doLogging = True
inputMode = "keyboard" #Change to joystick for PRODUCTION
currentWorkDirectory = os.getcwd()
pathToLogFolder = currentWorkDirectory + "/log/"
logFile = pathToLogFolder + str(datetime.date.today()) + "-" + str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second) + ".txt"
chosenMode = "none"
loaded = False



#You can define some sprites or images here
dirtTexture = pygame.image.load(currentWorkDirectory + "/assets/image/dirt_block.png")
grassTexture = pygame.image.load(currentWorkDirectory + "/assets/image/grass_block.png")
stoneTexture = pygame.image.load(currentWorkDirectory + "/assets/image/stone_block.png")
backGroundOne = pygame.image.load(currentWorkDirectory + "/assets/image/skybox_one.jpg")
goldStoneTexture = pygame.image.load(currentWorkDirectory + "/assets/image/gold_stone.png")
brickBlockTexture = pygame.image.load(currentWorkDirectory + "/assets/image/brick_block.png")
sfaCubeTexture = pygame.image.load(currentWorkDirectory + "/assets/image/sfa_cube.png")

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (153,0,153)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,128,0)
PINK = (255,51,153)
GRAY = (96,96,96)
TEAL = (51,255,255)
MAROON = (153,0,0)
LIME = (128,255,0)
NAVYBLUE = (0,0,153)
VIOLET = (204,153,255)
SKYBLUE = (28,92,140)

def createLog():
    if doLogging == False:
        return
    logfile = open(logFile, "w")
    logfile.write("Log Created\nPygame Version: {}\nPlatformer version: {}\nInputMode: {}\nDebugMode: {}\nCurrentDirectory: {}".format(pygame.version.ver, SCREEN_NAME, inputMode, debugMode, currentWorkDirectory)) #Writes some basic things upon creation
    logfile.close()

def writeLog(input):
    if doLogging == False:
        return
    logfile = open(logFile, "a")
    logfile.write("\n" + input) #Writes a new line given an input
    logfile.close()

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
    createLog()
    writeLog("Application starting")

    background = pygame.Surface(mainscreen.get_size())
    background = background.convert()
    background.fill(WHITE)

    #Platformer Game Level 1
    def levelOne():
        global loaded
        global mapLevel
        if loaded == False:
            loaded = True
            #do some initial things
            writeLog("Level one loading for first time")
            mapLevel = levelOneMap.level
        
        #mainscreen.fill(levelOneMap.skyColor)
        mainscreen.blit(pygame.transform.scale(pygame.image.load(currentWorkDirectory + levelOneMap.skyTexture), (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))  
       
        # open file in read mode
        with open('assets/levels/TestMap4.csv', 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for rowIndex, row in enumerate(csv_reader):
                for columnIndex, column in enumerate(row):
                    x = columnIndex * 64
                    y = rowIndex * 64
                    if column == '1':
                        mainscreen.blit(pygame.transform.scale(dirtTexture, (64,64)), (x,y))                    
                    elif column == '2':
                        mainscreen.blit(pygame.transform.scale(goldStoneTexture, (64,64)), (x,y))
                    elif column == '3':
                        mainscreen.blit(pygame.transform.scale(grassTexture, (64,64)), (x,y))
                    elif column == '4':
                        mainscreen.blit(pygame.transform.scale(sfaCubeTexture, (64,64)), (x,y))                    
                    elif column == '5':
                        mainscreen.blit(pygame.transform.scale(stoneTexture, (64,64)), (x,y))
                    elif column == '6':
                        mainscreen.blit(pygame.transform.scale(brickBlockTexture, (64,64)), (x,y))


        # mainscreen.fill(WHITE)
        # for x in range(SCREEN_HEIGHT//64):
        #     for i in range((SCREEN_WIDTH//64)+2):
        #         if x == 6:
        #             mainscreen.blit(pygame.transform.scale(grassTexture, (64,64)), (64*i,64*x))  
        #         elif x >= 9:
        #             randNumber = random.randint(1,10)
        #             if randNumber == 1:
        #                 mainscreen.blit(pygame.transform.scale(goldStoneTexture, (64,64)), (64*i,64*x))   
        #             else:
        #                 mainscreen.blit(pygame.transform.scale(stoneTexture, (64,64)), (64*i,64*x))   

        #         elif x == 8 or x == 7:
        #             mainscreen.blit(pygame.transform.scale(dirtTexture, (64,64)), (64*i,64*x))  
        #         else:
        #             #mainscreen.blit(pygame.transform.scale(backGroundOne, (SCREEN_WIDTH, SCREEN_HEIGHT - (64*6))), (0,0))  
        #             mainscreen.fill(SKYBLUE)
        # pygame.display.update()

    if inputMode == "keyboard":
        writeLog("Starting keyboard mode")
    elif inputMode == "joystick":
        writeLog("Starting joystick mode")
    else:
        writeLog("No input type selected, shutting down")
        return 1

    while True: #Main game loop
        for event in pygame.event.get(): #Loops through every event, can be keyboard or mouse input etc
            if event.type == pygame.QUIT:
                writeLog("Process ending, nominal shutdown")
                return 0
        if chosenMode == "none":
            #ask user to choose mode or pull up main screen or something
            chosenMode = "levelOne"
            writeLog("Level One mode chosen")
        if chosenMode == "levelOne":
            levelOne()
        clock.tick(60)
        #mainscreen.blit(background, (0,0))
        #pygame.draw.rect(background, NAVYBLUE, pygame.Rect(0,200,200,300))
        pygame.display.flip()

main()
