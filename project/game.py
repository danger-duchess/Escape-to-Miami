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

# import and resize picture of alligator
gatorPic = pg.image.load('alligator.png')
gatorPic = pg.transform.scale(gatorPic, (550, 500))


class Background(pg.sprite.Sprite):
    def __init__(self, background_pic, location):
        pg.sprite.Sprite.__init__(self)

        self.pic = pg.image.load(background_pic)
        self.box = self.pic.get_rect()
        self.box.left, self.box.top = location


# function to display gator in center of the screen


def button(text, x, y, width, height, color, presscolor, action=None):
    cursor = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pg.draw.rect(display, presscolor, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(display, color, (x, y, width, height))

    font2 = pg.font.Font("freesansbold.ttf", 20)
    buttontext = font2.render(text, True, (240, 10, 236))
    buttonbox = buttontext.get_rect()
    buttonbox.center = ((x + (width / 2)), (y + (height / 2)))

    display.blit(buttontext, buttonbox)


def menu_screen():
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # display picture
        display.fill((0, 0, 0))
        background = Background('miami-sunset.jpg', [0, 0])
        display.blit(background.pic, background.box)

        # create font and textbox to display title
        font = pg.font.Font('freesansbold.ttf', 64)
        title = font.render('Escape to Miami', True, (240, 10, 236))
        titleBox = title.get_rect()
        titleBox.center = (w * .5, h * .5)

        # put text box object on the center of the display object
        display.blit(title, titleBox)

        button("Begin!", 250, 450, 100, 50, (255, 255, 255), (0, 200, 0), game_loop)
        button("Quit", 650, 450, 100, 50, (255, 255, 255), (0, 200, 0), game_quit)

        pg.display.update()
        clock.tick(15)


# loop to run the game
def game_loop():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        # fill display black
        display.fill((0, 0, 0))
        pg.display.update()


def game_quit():
    pg.quit()


# start game
menu_screen()
# exit game
pg.quit()
