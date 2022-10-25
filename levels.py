import constants
import utilities
import pygame
from csv import reader

class levels:
    def __init__(self, screen, cwd, width, height):
        self.mainscreen = screen
        self.currentWorkDirectory = cwd
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height

    #Platformer Game Level 1
    def levelOne(self):
        loaded = False
        global mapLevel
        if loaded == False:
            loaded = True
            #do some initial things
            utilities.writeLog("Level one loading for first time")
            #mapLevel = levelOneMap.level
        
        #mainscreen.fill(levelOneMap.skyColor)
        self.mainscreen.blit(pygame.transform.scale(pygame.image.load(constants.skyTexture), (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))  
        
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
                        self.mainscreen.blit(pygame.transform.scale(constants.dirtTexture, (64,64)), (x,y))                    
                    elif column == '2':
                        self.mainscreen.blit(pygame.transform.scale(constants.goldStoneTexture, (64,64)), (x,y))
                    elif column == '3':
                        self.mainscreen.blit(pygame.transform.scale(constants.grassTexture, (64,64)), (x,y))
                    elif column == '4':
                        self.mainscreen.blit(pygame.transform.scale(constants.sfaCubeTexture, (64,64)), (x,y))                    
                    elif column == '5':
                        self.mainscreen.blit(pygame.transform.scale(constants.stoneTexture, (64,64)), (x,y))
                    elif column == '6':
                        self.mainscreen.blit(pygame.transform.scale(constants.brickBlockTexture, (64,64)), (x,y))
