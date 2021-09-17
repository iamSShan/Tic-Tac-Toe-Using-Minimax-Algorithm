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

# winner = None
# draw = None



# Initializing the pygame window
pg.init()

# Setting fps manually
FPS = 30
# To track time
CLOCK = pg.time.Clock()

# build the infrastructure of the display 
screen = pg.display.set_mode((width, height + 100), 0, 32)
# Set name of the window
pg.display.set_caption ('Tic-Tac-Toe')

# Loading the images as python object 
home_window = pg.image.load("images/logo.png")
x_img = pg.image.load("images/X.png")
o_img = pg.image.load("images/O.png")

# Resizing images 
home_window = pg.transform.scale(home_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80)) 
o_img = pg.transform.scale(o_img, (80, 80)) 


class Tictactoe:
    def __init__(self):
        self.winner = None
        self.draw = None
        # For storing the 'x' or 'o'
        self.player = 'x'


    def start_game(self):
        # Displaying home screen
        # blit is the method that enables pygame to display something over another thing.
        screen.blit(home_window, (0, 0))

        # Updating the display
        pg.display.update()
        time.sleep(3)
        # Removing home screen
        screen.fill(bg_color)
        
        # Drawing vertical and horizontal lines 
        pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
        pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
        pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
        pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
        self.draw_status()

    
    def draw_status(self):
        # Display status
        if self.winner is None: 
            message = self.player.upper() + "'s Turn"
        else: 
            message = self.winner.upper() + " won !"
        if self.draw: 
            message = "Game Draw !"
       
        # Setting a font object 
        font = pg.font.Font(None, 30) 
          
        # Setting the font properties like color and width of the text 
        text = font.render(message, 1, (255, 255, 255)) 
       
        # Display the status at the bottom of the rendered window
        screen.fill((0, 0, 0), (0, 500, 600, 100)) 
        text_rect = text.get_rect(center =(width / 2, 600-50)) 
        screen.blit(text, text_rect) 
        pg.display.update() 
      

    def check_win(self): 
        global board 
       
        # checking for winning rows 
        for row in range(0, 3): 
            if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)): 
                self.winner = board[row][0] 
                pg.draw.line(screen, (250, 0, 0), 
                             (0, (row + 1)*height / 3 -height / 6), 
                             (width, (row + 1)*height / 3 - height / 6 ), 
                             4) 
                break
       
        # checking for winning columns 
        for col in range(0, 3): 
            if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)): 
                self.winner = board[0][col] 
                pg.draw.line (screen, (250, 0, 0), ((col + 1)* width / 3 - width / 6, 0), ((col + 1)* width / 3 - width / 6, height), 4) 
                break
           
        # check for diagonal winners 
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None): 
              
            # game won diagonally left to right 
            self.winner = board[0][0] 
            pg.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4) 
              
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None): 
              
            # game won diagonally right to left 
            self.winner = board[0][2] 
            pg.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4) 
       
        if(all([all(row) for row in board]) and self.winner is None ): 
            self.draw = True
        self.draw_status() 


    def drawXO(self, row, col): 
        global board 
          
        # for the first row, the image 
        # should be pasted at a x coordinate 
        # of 30 from the left margin 
        if row == 1: 
            posx = 30
              
        # for the second row, the image  
        # should be pasted at a x coordinate  
        # of 30 from the game line      
        if row == 2: 
      
            # margin or width / 3 + 30 from  
            # the left margin of the window 
            posx = width / 3 + 30
              
        if row == 3: 
            posx = width / 3 * 2 + 30
       
        if col == 1: 
            posy = 30
              
        if col == 2: 
            posy = height / 3 + 30
          
        if col == 3: 
            posy = height / 3 * 2 + 30
              
        # setting up the required board  
        # value to display 
        board[row-1][col-1] = self.player 
          
        if(self.player == 'x'): 
              
            # pasting x_img over the screen  
            # at a coordinate position of 
            # (pos_y, posx) defined in the 
            # above code 
            screen.blit(x_img, (posy, posx)) 
            self.player = 'o'
          
        else: 
            screen.blit(o_img, (posy, posx)) 
            self.player = 'x'
        pg.display.update() 

    def user_click(self): 
        # Get coordinates of mouse click 
        x, y = pg.mouse.get_pos() 
       
        # Get column of mouse click (1-3) 
        if(x<width / 3): 
            col = 1
          
        elif (x<width / 3 * 2): 
            col = 2
          
        elif(x<width): 
            col = 3
          
        else: 
            col = None
       
        # Get row of mouse click (1-3) 
        if(y<height / 3): 
            row = 1
          
        elif (y<height / 3 * 2): 
            row = 2
          
        elif(y<height): 
            row = 3
          
        else: 
            row = None
            
        # After getting the row and col, we need to draw the images at the desired positions 
        if(row and col and board[row-1][col-1] is None): 
            self.drawXO(row, col) 
            self.check_win() 


    def reset_game(self):
        global board
        time.sleep(3)
        self.player = 'x'
        self.draw = False
        self.start_game()
        self.winner = None
        board = [[None]*3, [None]*3, [None]*3]


if __name__ == "__main__":

    ttt = Tictactoe()
    ttt.start_game()

    while(True):
        for event in pg.event.get():
            # If quitting the game
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type is MOUSEBUTTONDOWN:
                # The user has clicked
                ttt.user_click()
                if ttt.winner or ttt.draw:
                    ttt.reset_game()
        pg.display.update()
        CLOCK.tick(FPS)
