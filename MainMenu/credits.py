import pygame, sys

class credits:

    def __init__(self, screen, fpsClock):
        # define the pygame main window surface object.
        self.MAIN_WINDOW_SURFACE = screen

        # define the pygame.time.Clock object to control the frames refresh frequency.
        self.FRAME_PER_SECOND_CLOCK = fpsClock

        # define the frame per second numbers, that means one second draw 23 frame at most.
        self.FPS = 10

        # define the text surface object.
        self.TEXT_SURFACE_OBJECT = None

        # define the direction constants.
        self.UP = 'UP'

        # the text move steps.
        self.MOVE_STEP = 5

        # define the text surface rectangle's center (x, y) coordinates.
        self.TEXT_CENTER_X = 0
        self.TEXT_CENTER_Y = 0


    # this function initialize the pygame application.
    def initialize_pygame():
        
        pygame.init()
        
        # create the game main window.
        main_window_size = (1000, 300)
        
        global MAIN_WINDOW_SURFACE
        MAIN_WINDOW_SURFACE = pygame.display.set_mode(main_window_size, pygame.RESIZABLE)
        
        # set the window title.
        window_title = 'Pygame Draw Moving Text With Specified Text Font Example.'
        pygame.display.set_caption(window_title)
            
        # create a pygame.time.Clock object.
        global FRAME_PER_SECOND_CLOCK
        FRAME_PER_SECOND_CLOCK = pygame.time.Clock()
        
    
    # get a text font from the system supported font list.    



    # initialize the moving text surface object.    
    def initialize_moving_text():
                
        text_font = pygame.font.Font('freesansbold.ttf', 12)
        
        # define the text color and text background color.
        text_color = pygame.Color('white')
        text_background_color = pygame.Color('black')

        global TEXT_SURFACE_OBJECT
        # call the pygame.font.Font's object's render() method to create the text surface object.
        TEXT_SURFACE_OBJECT = text_font.render('Thank you for playing our game', True, text_color, text_background_color) 
        
        # get the pygame main screen window's width and height.
        window_width = MAIN_WINDOW_SURFACE.get_width()
        window_height = MAIN_WINDOW_SURFACE.get_height()
        
        # calculate the text surface object's rectangle object's center coordinates.
        global TEXT_CENTER_X
        global TEXT_CENTER_Y
        
        # when the pygame starts, the text surface object is located at the main window screen center.
        if TEXT_CENTER_X ==0:
            
            TEXT_CENTER_X = window_width/2
            TEXT_CENTER_Y = window_height/2
        
        # get the text surface object's pygame.Rect object.
        text_rect_object = TEXT_SURFACE_OBJECT.get_rect()
        # position the text rectangle object' center to coordinate(TEXT_CENTER_X, TEXT_CENTER_Y).
        text_rect_object.center = (TEXT_CENTER_X, TEXT_CENTER_Y)    
        
        # clear the main window screen by drawing white color.
        MAIN_WINDOW_SURFACE.fill(pygame.Color('black'))
        # draw the text surface object to the pygame main window.    
        MAIN_WINDOW_SURFACE.blit(TEXT_SURFACE_OBJECT, text_rect_object)

    # this function will move the text on the screen by changing the text surface object center point coordinates. 
    def draw_moving_text(self):
        
        global TEXT_CENTER_Y
        # if move to left.
        if self.UP:
            # text center point's x coordinate will decrease.
            TEXT_CENTER_Y -= self.MOVE_STEP
        
        
        # get the main window's width.
        window_width = MAIN_WINDOW_SURFACE.get_width()
        
            
        # if the text move to the main window screen center.
        if TEXT_CENTER_X == window_width/2:
            # change the text font.  
            self.initialize_moving_text()
        else:
            # get the text surface object's rectangle object.    
            text_rect_object = TEXT_SURFACE_OBJECT.get_rect()
            # position the text surface object to coordinates (TEXT_CENTER_X, TEXT_CENTER_Y).
            text_rect_object.center = (TEXT_CENTER_X, TEXT_CENTER_Y)    
            # clear the window by fill the white background color.
            MAIN_WINDOW_SURFACE.fill(pygame.Color('white'))
            # draw the text surface object to the main window screen with the pygame.Rect position.
            MAIN_WINDOW_SURFACE.blit(TEXT_SURFACE_OBJECT, text_rect_object)
        

    def main_loop(self):
        
        while True:
            
            self.draw_moving_text()
            
            # Loop to get events and listen for event status.
            for event in pygame.event.get():
                
                # if user click the window close button.
                if event.type == pygame.QUIT: 
                                
                    # quit pygame.
                    pygame.quit()
                    
                    # quit the application.
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        
                        print('The Esc key is pressed.')
                        
                        # quit pygame.
                        pygame.quit()
                    
                        # quit the application.
                        sys.exit()
                        
                elif event.type == pygame.VIDEORESIZE:
                    
                    # draw the pixel units again when user resize the pygame window. 
                    self.draw_moving_text()
                        
        
            pygame.display.update()
            
            # set the frame count that will be printed in one seconds. 
            FRAME_PER_SECOND_CLOCK.tick(self.FPS)

    if __name__ == '__main__':
        
        initialize_pygame()
        
        initialize_moving_text()
        
        main_loop()
        