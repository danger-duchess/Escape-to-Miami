import pygame as pg
from pygame import font
from extraction import scenario
import textwrap

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

# define color tuples here
magenta = (240, 10, 236)
black = (0, 0, 0)
white = (255, 255, 255)

# defining text wrapping dimensions
wrap_options = {'extra_large': [90, 8, 90],
                'large': [50, 16, 45],
                'medium': [36,24,20],
                'small': [15,60,10]}

# create the display window
display = pg.display.set_mode([w, h])

# set the name of the game window
pg.display.set_caption('Escape to Miami')

# import and resize picture of alligator
gatorPic = pg.image.load('alligator.png')
gatorPic = pg.transform.scale(gatorPic, (550, 500))


# function to quit game if quit button is pressed
def game_quit():
    pg.quit()


# class to create title screen background
class Background(pg.sprite.Sprite):
    # constructor
    def __init__(self, background_pic, location):
        pg.sprite.Sprite.__init__(self)

        self.pic = pg.image.load(background_pic)
        self.box = self.pic.get_rect()
        self.box.left, self.box.top = location


# function to define a button press, with dimensions, location, colors, and actions
def button(text, x, y, width, height, presscolor, action=None):
    cursor = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # button is being hovered over
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pg.draw.rect(display, presscolor, (x, y, width, height))
        # button is pressed
        if click[0] == 1 and action is not None:
            action()

    # Render button boxes and text
    font2 = pg.font.Font('BOYCOTT_.ttf', 24)
    buttontext = font2.render(text, True, magenta)
    buttonbox = buttontext.get_rect()
    buttonbox.center = ((x + (width / 2)), (y + (height / 2)))

    display.blit(buttontext, buttonbox)


# function to display start/menu screen
def menu_screen():
    running = True

    while running:
        # ways to quit game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # display picture
        display.fill((0, 0, 0))
        background = Background('miami-sunset.jpg', [0, 0])
        display.blit(background.pic, background.box)

        # create font and textbox to display title
        font = pg.font.Font('After_Shok.ttf', 64)
        title = font.render('Escape to Miami', True, magenta)
        titlebox = title.get_rect()
        titlebox.center = (w * .5, h * .5)

        # put text box object on the center of the display object
        display.blit(title, titlebox)

        # display begin and quit buttons
        button('Begin', 250, 450, 100, 50, white, game_loop)
        button('Quit', 650, 450, 100, 50, white, game_quit)

        pg.display.update()
        clock.tick(15)


# loop to run the actual game when begin button is pressed
def game_loop():
    running = True

    while running:
        # ways to quit game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # fill display black
        display.fill((0, 0, 0))
        font3 = pg.font.SysFont('Arial', 15)
        scenario_text = font3.render(scenario, True, white)
        scenario_box = scenario_text.get_rect()
        scenario_box.center = (w * .5, h * .5)
        display.blit(scenario_text, scenario_box)

        pg.display.update()


# start game
menu_screen()

# exit game
pg.quit()
