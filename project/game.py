import pygame as pg
from random import randint
from random import choice
from pygame import font
from extraction import scenario
from project.car import Car
from project.inventory import Inventory
import textwrap

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_1,
    K_2,
    K_n,
    K_i,
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
    "Only 223 miles to go! Let's see what happens as you escape to Miami"]
# random encounters to be selected in game
choice_based = [
    dict(type='gas station',
         script='You arrive at a gas station. You can stop and buy fuel now, or keep going. What do you do?',
         choices=['1. Enter Store', '2. Keep Driving'],
         outcomes1=['You refuel your gas. That will help later!',
                    'Turns out it was deserted! You actually lost fuel from this!'],
         outcomes2=['You keep moving along.', 'You probably probably needed fuel.']),
    dict(type='Sublix',
         script='Mmm, smell that? It smells like the bakery at Sublix just finished baking bread for their subs. Do you buy one?',
         choices=['1. Buy that sub!', '2. I hate subs.'],
         outcomes1=['You buy a sub!', 'The Sub was rancid. You lose health!'],
         outcomes2=['You keep moving along', 'You were hungry. That was a mistake.']),
    dict(type='rest stop',
         script="You reach a classic Turnpike Reststop. (Strange you weren't on the turnpike.) You could stop and fix your car here! Maybe get some food! What do you do?",
         choices=['1. Stay at the Rest Stop', '2. Keep on Trucking'],
         outcomes1=['Your car is fixed!',
                    "Turns out you don't know how to fix cars, so you actually make it worse."],
         outcomes2=['You keep moving along.', 'Well, you could have used the pit stop.']),
    dict(type="swamp",
         script="Hmm, somewhere along the drive, you hit a swamp. Funny how that works. You could go around but it might take longer to get to Miami. What do you do?",
         choices=['1. Go through the swamp', '2. Go around'],
         outcomes1=["Huh. Somehow by dumb luck, you got through the swamp unscathed.",
                    "You drove through it...somehow. Too bad your car took damage. It's a car. Not an ATV."],
         outcomes2=["You drive around the swamp but you're now further from Miami.",
                    "Turns out it was just on the side of the road. You were looking out the wrong window."])]
true_random = [dict(type="traffic jam",
                    script="Uh oh, you entered a traffic jam! It'll take hours to get out of this. ",
                    outcomes=["Oh, that cleared up fast. Looks like you didn't lose much gas.",
                              "You lost so much gas and you didn't even move."]),
               dict(type="alligator road",
                    script="Alligators are sunning in front of your car.",
                    outcomes=["Your car spooked them! Luckily, they're too scared to do anything!",
                              "Your car spooked them! One alligator hates it! They bite your car!"]),
               dict(type='scenario',
                    script=scenario,
                    outcomes=["You fight them off! They give you an item as payment!",
                              "You've been defeated by their craziness! You lose health and condition."])]
# variables for player and distance needed to be covered
milesfrommiami = 223  # actual distance from Shingle Creek to Miami
player_car = Car()
p_inventory = Inventory()


# function to quit game if quit button is pressed
def game_quit():
    pg.quit()


# function to display text, pass align in to put text where you want it
# off used as offset (use when text is being stacked somewhere)
def message_display(text, align, offh=0, offw=0):
    font = pg.font.SysFont('Arial', 15)
    message = font.render(text, True, (255, 255, 0))
    textRect = message.get_rect()
    if align == "center":
        textRect.center = ((w * 0.5) + offw, (h * 0.5) + offh)
        display.blit(message, textRect)
    elif align == "right":
        display.blit(message, textRect)
    elif align == "left":
        display.blit(message, textRect)
    elif align == "bottomright":
        textRect.bottomright = (w + offw, h + offh)
        display.blit(message, textRect)
    elif align == "bottomleft":
        textRect.bottomleft = (0 + offw, h + offh)
        display.blit(message, textRect)
    elif align == "topright":
        textRect.topright = (w + offw, 0 + offh)
        display.blit(message, textRect)
    elif align == "topleft":
        textRect.topleft = (0 + offw, 0 + offh)
        display.blit(message, textRect)


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
    if n == 0:
        message_display(player_car.issueRandom(), "center")
    elif n == 1:
        r1 = randint(0, 1)
        if r1 == 0:
            choice_dict = choice(choice_based)  # choose an index from the choice based ones
            script = choice_dict['script']
            choices = choice_dict['choices']
            font = pg.font.SysFont('Arial', 15)
            message = font.render(script, True, (255, 255, 0))
            textRect = message.get_rect()
            textRect.center = (w * .5, h * .5)
            display.blit(message, textRect)
            event = pg.event.wait()
            choice_button(choices[0], 250, 450, 100, 50, white)
            choice_button(choices[1], 650, 450, 100, 50, white)
            pg.display.update()
            running = True
            while running:
                for events in pg.event.get():
                    if events.type == KEYDOWN:
                        if events.key == K_1:
                            player_choice1(choice_dict)
                            running = False
                        if events.key == K_2:
                            player_choice2(choice_dict)
                            running = False

        elif r1 == 1:
            choice_dict = choice(true_random)
            script = choice_dict['script']
            message_display(script, "center")
            true_random_outcome(choice_dict)


# choice for player button 1
def player_choice1(event_dict):
    outcomes = event_dict['outcomes1']
    result = ''
    outcome = randint(0, 1)

    if event_dict['type'] == 'gas station':
        refuel = randint(0, 25)
        if outcome == 0:
            player_car.setFuel(refuel)
            result = "You refilled your tank with %d units of gas" % refuel
        elif outcome == 1:
            player_car.setFuel(-refuel)
            result = "You lost %d units of gas" % refuel
    elif event_dict['type'] == 'Sublix':
        if outcome == 0:
            if not p_inventory.addItem("sub"):
                result = "Your inventory is full! You can't add anymore items."
            else:
                result = "A sub has been added to your inventory!"
                p_inventory.addItem("sub")
        elif outcome == 1:
            damage = randint(0, 25)
            player_car.setHealth(-damage)
            result = "You lost %d health" % damage
    elif event_dict['type'] == 'rest stop':
        if outcome == 0:
            fix = 100 - player_car.getCondition()
            player_car.setCondition(fix)
            result = "Your car's condition is at %d percent!" % player_car.getCondition()
        elif outcome == 1:
            fix = randint(0, 50)
            player_car.setCondition(-fix)
            result = "Your car's condition is at %d percent!" % player_car.getCondition()
    else:
        milescovered = randint(0, 20)
        if outcome == 0:
            player_car.updatePosition(milescovered)
            result = "You are now %d miles closer to Miami" % milescovered
        if outcome == 1:
            condition = randint(0, 25)
            player_car.setCondition(-condition)
            result = "Your car is at %d condition, but you are %d miles closer to Miami" % (
                player_car.getCondition(), milescovered)
    final_outcome = outcomes[outcome] + "" + result
    message_display(final_outcome, "center", 20)
    pg.display.update()


# choice for player button 2
def player_choice2(event_dict):
    outcomes = event_dict['outcomes2']
    result = ''
    outcome = randint(0, 1)
    if event_dict['type'] == 'gas station':
        refuel = randint(0, 25)
        if outcome == 0:
            pass
        elif outcome == 1:
            player_car.setFuel(-refuel)
            result = "You lost %d units of gas" % refuel
    elif event_dict['type'] == 'Sublix':
        if outcome == 0:
            pass
        elif outcome == 1:
            damage = randint(0, 25)
            player_car.setHealth(-damage)
            result = "You take %d health loss as a result." % damage
    elif event_dict['type'] == 'rest stop':
        if outcome == 0:
            pass
        elif outcome == 1:
            fix = randint(0, 50)
            player_car.setCondition(-fix)
            result = "Your car's condition is at %d percent!" % player_car.getCondition()
    else:
        milescovered = randint(0, 20)
        if outcome == 0:
            player_car.updatePosition(milescovered)
            result = "You are now %d miles closer to Miami" % milescovered
        elif outcome == 1:
            player_car.updatePosition(-milescovered)
            result = "You are %d miles further from Miami" % milescovered
    final_outcome = outcomes[outcome] + " " + result
    message_display(final_outcome, "center", 20)
    pg.display.update()


def true_random_outcome(event_dict):
    outcomes = event_dict['outcomes']
    result = ""
    outcome = randint(0, 1)
    condition = player_car.getCondition()
    health = player_car.getHealth()
    fuel = player_car.getFuel()
    if event_dict['type'] == "traffic jam":
        if outcome == 0:
            lostfuel = randint(0, 10)
            player_car.setFuel(-lostfuel)
            result = "You only lost %d fuel!" % lostfuel
        elif outcome == 1:
            lostfuel = randint(0, 50)
            player_car.setFuel(-lostfuel)
            result = "You lost %d fuel. That sucks." % lostfuel
    elif event_dict['type'] == "alligator road":
        if outcome == 0:
            result = "It must be your lucky day!"
        elif outcome == 1:
            bite = randint(0, 35)
            player_car.setCondition(-bite)
            result = "You lose %d condition. Damn, that's a nasty bite!" % bite
    else:
        if outcome == 0:
            if condition < fuel and condition < health:
                if p_inventory.addItem("Spare Tire"):
                    result = "You got a spare tire to fix your condition!"
                else:
                    result = "Too bad. Your inventory is too full."
            elif fuel < health and fuel < condition:
                if p_inventory.addItem("Fuel Can"):
                    result = "You get a can of fuel to refuel your car!"
                else:
                    result = "Too bad. Your inventory is too full."
            elif health < fuel and health < condition:
                if p_inventory.addItem("Florida Orange"):
                    result = "You get a juicy Florida orange to get your health back on track!"
                else:
                    result = "Too bad. Your inventory is too full."
        elif outcome == 1:
            damage = randint(0, 25)
            con_lost = randint(0, 25)
            player_car.setHealth(-damage)
            player_car.setCondition(-con_lost)
            result = "You lose %d health and %d condition" % (damage, con_lost)
    final_outcome = outcomes[outcome] + " " + result
    message_display(final_outcome, "center")
    pg.display.update()


def inventory_use():
    health = player_car.getHealth()
    condition = player_car.getCondition()
    fuel = player_car.getFuel()
    result = ""
    background = Background("trunk.jpg")
    background.pic = pg.transform.scale(background.pic, (w, h))
    if condition < fuel and condition < health:
        if p_inventory.useItem("Spare Tire"):
            player_car.setCondition(25)
            result = "You use your spare tire to fix the car."
        elif p_inventory.useItem("Florida Man Car Repair Coupon"):
            player_car.setCondition(100)
            result = "You use the Florida Man coupon! Your car is in tiptop shape!"
        else:
            pass
    elif fuel < health and fuel < condition:
        if p_inventory.useItem("Fuel Can"):
            player_car.setFuel(25)
            result = "You use a can of fuel to refuel your car!"
        else:
            pass
    elif health < fuel and health < condition:
        if p_inventory.addItem("Florida Orange"):
            player_car.setHealth(15)
            result = "You eat a juicy Florida orange to get your health back on track!"
        elif p_inventory.useItem("Sub"):
            player_car.setHealth(25)
            result = "You eat that Sublix sub to restore your health!"
        else:
            pass
    else:
        result = "You have nothing to fix right now! You save your items for later."
    message_display(result, "center", 20)
    pg.display.update()


def inventory_display():
    print("in inventory")
    length, inventory_array = p_inventory.getInventory()
    items = []
    background = Background("trunk.jpg", [0, 0])
    background.pic = pg.transform.scale(background.pic, (w, h))
    if length == 0:
        message = "You have no items."
        message_display(message, "center")
        running = True
        while running:
            for events in pg.event.get():
                if events.type == KEYDOWN:
                    if events.key == K_n:
                        game_loop()
                        running = False
    else:
        for keys in inventory_array.keys():
            items.append(keys)
        names = str(items)
        message = "You have %d items, use one? Your items are %s" % (length, names)
        message_display(message, "center")
        choice_button("1. Yes", 250, 450, 100, 50, (255, 255, 0))
        choice_button("2. No", 650, 450, 100, 50, (255, 255, 0))
        running = True
        while running:
            for events in pg.event.get():
                if events.type == KEYDOWN:
                    if events.key == K_1:
                        inventory_use()
                        running = False
                    if events.key == K_2:
                        game_loop()
                        running = False
    pg.display.update()


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


def choice_button(text, x, y, width, height, presscolor, action=None):
    cursor = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    # button is being hovered over
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pg.draw.rect(display, presscolor, (x, y, width, height))
        # button is pressed
        if click[0] == 1 and action is not None:
            action()

    # Render button boxes and text
    font2 = pg.font.SysFont('Arial', 15)
    buttontext = font2.render(text, True, (255, 255, 0))
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
        button('Begin', 250, 450, 100, 50, white, intro_screen)
        button('Quit', 650, 450, 100, 50, white, game_quit)

        pg.display.update()
        clock.tick(15)


def reset_stats():
    player_car.reset()
    p_inventory.emptyInv()


def intro_screen():
    running = True
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
                    if i == len(intro_script):
                        game_loop()

        if i < len(intro_script):
            background1 = Background("shingle-creek-00.jpg", [0, 0])
            background1.pic = pg.transform.scale(background1.pic, (w, h))
            display.blit(background1.pic, background1.box)
            message = intro_script[i]
            message_display(message, "center")

        pg.display.update()

        clock.tick(15)


# loop to run the actual game when begin button is pressed
def game_loop():
    running = True
    turnend = False
    turns = 0
    reset_stats()
    background1 = Background("road.jpg", [0, 0])
    background1.pic = pg.transform.scale(background1.pic, (w, h))
    display.blit(background1.pic, background1.box)
    # pg.display.update()
    i = 0
    info(turns)

    while running:
        i += 1

        background1 = Background("road.jpg", [0, 0])
        background1.pic = pg.transform.scale(background1.pic, (w, h))
        display.blit(background1.pic, background1.box)

        # add first image for background
        event = pg.event.wait()
        # ways to quit game
        if event.type == pg.QUIT:
            game_quit()
        if event.type == KEYDOWN:
            if event.key == K_n:
                nextTurn(turns)
                pg.display.update()
                turns += 1
            elif event.key == K_i:
                print("clicked!")
                inventory_display()
                pg.display.update()

        if player_car.getPosition() == milesfrommiami:
            win()
        if player_car.is_dead():
            running = False
            lose()


def nextTurn(turns):
    if player_car.getPosition() != milesfrommiami:
        info(turns)
        if player_car.getCondition() == 0:
            player_car.setHealth(-1)
            player_car.setFuel(-player_car.getFuel())
        if player_car.getFuel() == 0:
            player_car.setCondition(-player_car.getCondition())

        eventopt = randint(0, 1)
        if eventopt == 0:
            message = "What a beautiful day on I-75"
            message_display(message, "center")
            player_car.updatePosition()
        if eventopt == 1:
            RandomEvent(randint(0, 1))
        if player_car.is_dead() is True:
            if p_inventory.useItem("sub"):
                player_car.setHealth(25)
                message = "You almost died! But you ate your sub, getting 25 health back!"
                message_display(message, "center")
            else:
                running = False

        player_car.setFuel(-1)


def info(turns):
    # displays all important info for Items
    message = "Turn " + str(turns)
    message_display(message, "topright")
    message = "Player Health: " + str(player_car.getHealth())
    message_display(message, "topleft")
    message = "Car Condition: " + str(player_car.getCondition())
    message_display(message, "topleft", 15)
    message = "Car Fuel: " + str(player_car.getFuel())
    message_display(message, "topleft", 30)
    message = "Car Speed: " + str(player_car.getSpeed()) + " official Florida unit per mile"
    message_display(message, "topleft", 45)
    message = "Inventory: "
    message_display(message, "bottomleft", -45)
    status = "You are " + str(
        milesfrommiami - player_car.getPosition()) + " miles away from Miami"
    message_display(status, "bottomright")
    i_amt, i_inv = p_inventory.getInventory()
    if i_amt == 0:
        message = "Empty"
        message_display(message, "bottomleft")
    else:
        message = str(i_amt) + " Items"
        message_display(message, "bottomleft", 0)


def win():
    background1 = Background("road.jpg", [0, 0])
    background1.pic = pg.transform.scale(background1.pic, (w, h))
    display.blit(background1.pic, background1.box)
    font = pg.font.Font('After_Shok.ttf', 64)

    title = font.render('You Won!!!!!', True, magenta)
    titlebox = title.get_rect()
    titlebox.center = (w * .5, h * .5)

    # put text box object on the center of the display object
    display.blit(title, titlebox)

    pg.display.update()


def lose():
    background1 = Background("road.jpg", [0, 0])
    background1.pic = pg.transform.scale(background1.pic, (w, h))
    display.blit(background1.pic, background1.box)
    font = pg.font.Font('After_Shok.ttf', 64)
    title = font.render('You Died!', True, magenta)
    titlebox = title.get_rect()
    titlebox.center = (w * .5, h * .5)
    message_display("You were " + str(223 - player_car.getPosition()) + " miles from Miami", "center", 150)

    # put text box object on the center of the display object
    display.blit(title, titlebox)

    pg.display.update()
    pg.time.wait(5000)
    menu_screen()


# start game
menu_screen()

# exit game
pg.quit()