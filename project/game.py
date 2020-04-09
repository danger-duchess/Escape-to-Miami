import pygame as pg
from random import randint
from pygame import font
from extraction import scenario
from project.car import Car
import textwrap

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_n,
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
                'medium': [36, 24, 20],
                'small': [15, 60, 10]}

# create the display window
display = pg.display.set_mode([w, h])

# set the name of the game window
pg.display.set_caption('Escape to Miami')

# import and resize picture of alligator
gatorPic = pg.image.load('alligator.png')
gatorPic = pg.transform.scale(gatorPic, (550, 500))

# story script for first part of game
intro_script = [
    "Press n to continue at the end of the script",
    "It's a beautiful, swampy day near Shingle Creek, Florida, the headwaters of the Everglades. Normally, you'd be fine with this but you're bored. So bored.",
    "You decide to take that car for a spin through the Everglades until you get to Miami.",
    "Only 233 miles to go! Let's see what happens as you escape to Miami"]

# variables for player and distance needed to be covered
milesfrommiami = 223
player_car = Car()


# function to quit game if quit button is pressed
def game_quit():
    pg.quit()


# function to display text
def message_display(text):
    font = pg.font.SysFont('Arial', 15)
    message = font.render(text, True, (255, 255, 0))
    textRect = message.get_rect()
    textRect.center = (w * .5, h * .5)
    display.blit(message, textRect)
    pg.display.update()


# class to create title screen background
class Background(pg.sprite.Sprite):
    # constructor
    def __init__(self, background_pic, location):
        pg.sprite.Sprite.__init__(self)

        self.pic = pg.image.load(background_pic)
        self.box = self.pic.get_rect()
        self.box.left, self.box.top = location


# function to generate a random event
def RandomEvent(n):

    if n is 0:
        message_display(player_car.issueRandom())
    if n is 1:
        message_display(scenario)
    if n is 2:
        message_display()



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
    # variable to iterate through intro
    turnend = False
    turns = 0
    i = 0
    while running:
        # ways to quit game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_n:
                    # iterate through intro script until end is reached
                    if i < len(intro_script):
                        i += 1
                    else:
                        pass
        display.fill((0, 0, 0))
        # add first image for background
        background1 = Background("shingle-creek-00.jpg", [0, 0])
        background1.pic = pg.transform.scale(background1.pic, (w, h))
        display.blit(background1.pic, background1.box)

        message = intro_script[i]
        message_display(message)
        if i is len(intro_script):
            while player_car.getPosition() is not milesfrommiami:
                message = "Turn " + turns
                message_display(turns)
                if player_car.getCondition() is 0:
                    player_car.setHealth()
                eventopt = randint(0, 1)
                if eventopt is 0:
                    player_car.updatePosition()
                    player_car.setFuel()
                    status = "You are " + (milesfrommiami - player_car.getPosition()) + "miles away from Miami"
                    message_display(status)
                    turns += 1
                    turnend = True
                if eventopt is 1:
                    RandomEvent()


# start game
menu_screen()

# exit game
pg.quit()
