import pygame as pg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT, )

# initialize pygame
pg.init()

# create time variable
clock = pg.time.Clock()

# define screen height and width variables
w, h = 1000, 600

# create the display window
display = pg.display.set_mode([w, h])

# set the name of the game window
pg.display.set_caption('Escape to Miami')

# create font and textbox to display title
font = pg.font.Font('freesansbold.ttf', 64)
title = font.render('Escape to Miami', True, (240, 10, 236))
titleBox = title.get_rect()
titleBox.center = (w * .73, h * .5)

# import and resize picture of alligator
gatorPic = pg.image.load('alligator.png')
gatorPic = pg.transform.scale(gatorPic, (550, 500))


# function to display gator in center of the screen
def gator():
    display.blit(gatorPic, (w * .01, h * .1))


# loop to run the game
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # fill display black
    display.fill((0, 0, 0))
    # display picture
    gator()
    # put text box object on the center of the display object
    display.blit(title, titleBox)
    pg.display.update()

# exit game
pg.quit()
