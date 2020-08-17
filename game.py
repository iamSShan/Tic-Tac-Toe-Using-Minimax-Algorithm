# Import necessary libraries
import sys
import time
import pygame as pg
from pygame.locals import *

# Window details
width = 500
height = 500
bg_color = (255, 255, 255)  # white
line_color = (0, 0, 0)  # black
board = [[None]*3, [None]*3, [None]*3]  # 3x3 board

winner = None
draw = None

# For storing the 'x' or 'o' 
player = 'x'

# Initializing the pygame window
pg.init()

# Setting fps manually
fps = 30
# To track time
CLOCK = pg.time.Clock()

# build the infrastructure of the display 
board = pygame.display.set_mode ((300, 325))
# Set name of the window
pg.display.set_caption ('Tic-Tac-Toe')

# Loading the images as python object 
home_window = pg.image.load("logo.jpg") 
x_img = pg.image.load("X.png") 
o_img = pg.image.load("O.png") 

# Resizing images 
home_window = pg.transform.scale(home_window, (width, height + 100)) 
x_img = pg.transform.scale(x_img, (80, 80)) 
o_img = pg.transform.scale(o_img, (80, 80)) 


class Tictactoe:
    def __init__(self):
        pass

    def start_game(self):
        # blit is the method that enables pygame to display something over another thing.
        screen.blit(home_window, (0, 0))

        # updating the display
        pg.display.update()
        time.sleep(3)
        screen.fill(bg_color)
        
        # drawing vertical and horizontal lines       
        pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
        pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
        pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
        pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
        self.draw_status()


    def reset_game(self):
        global winner, draw, board
        time.sleep(3)
        player = 'x'
        draw = False
        start_game()
        winner = None
        board = [[None]*3, [None]*3, [None]*3]

if __name__ == "__main__":

    ttt = Tictactoe()
    ttt.start_game()

    while(True):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                # The user has clicked
                ttt.user_click()
                if winner or draw:
                    ttt.reset_game()
        pg.display.update()
        CLOCK.tick(fps)        

