import pygame
import utilities

# Current Directory
currentWorkDirectory = utilities.currentWorkDirectory

#You can define some sprites or images here
dirtTexture = pygame.image.load(currentWorkDirectory + "/assets/image/dirt_block.png")
grassTexture = pygame.image.load(currentWorkDirectory + "/assets/image/grass_block.png")
stoneTexture = pygame.image.load(currentWorkDirectory + "/assets/image/stone_block.png")
backGroundOne = pygame.image.load(currentWorkDirectory + "/assets/image/skybox_one.jpg")
goldStoneTexture = pygame.image.load(currentWorkDirectory + "/assets/image/gold_stone.png")
brickBlockTexture = pygame.image.load(currentWorkDirectory + "/assets/image/brick_block.png")
sfaCubeTexture = pygame.image.load(currentWorkDirectory + "/assets/image/sfa_cube.png")
skyTexture = pygame.image.load(currentWorkDirectory + "/assets/image/skybox_one.jpg")

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