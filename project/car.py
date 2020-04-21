# Escape to Miami

from random import seed
from random import randint

seed()


class Car:
    def __init__(self):
        self._health = 100
        self._fuel = 100
        self._condition = 100
        self._speed = 1
        self._position = 0

    # resets the players stats when game is started up (kind of a second constructor call)
    def reset(self):
        self._health = 100
        self._fuel = 100
        self._condition = 100
        self._speed = 1
        self._position = 0

    # next 6 functions all set and get certain private variables
    def getHealth(self):
        return self._health

    def setHealth(self, n):
        self._health += n
        if self._health <= 0:
            self._health = 0
        elif self._health > 100:
            self._health = 100

    def getFuel(self):
        return self._fuel

    def setFuel(self, n):
        self._fuel += n
        if self._fuel <= 0:
            self._fuel = 0
        elif self._fuel > 100:
            self._fuel = 100

    def getCondition(self):
        return self._condition

    # when condition changes, car will slow down or speed up depending on if n is negative or positive
    def setCondition(self, n):
        self._condition += n
        if self._condition <= 0:
            self._condition = 0
        elif self._condition > 100:
            self._condition = 100
        n *= 0.01
        self.updateSpeed(n)

    def updateSpeed(self, n):
        self._speed += n

    def getSpeed(self):
        return self._speed

    def getPosition(self):
        return self._position

    # position is purely based on speed
    def updatePosition(self, miles_covered=0):
        if self.getCondition() is 0:
            self._speed = 0.1
        self._position = self._position + self.getSpeed()
        if miles_covered != 0:
            self._position += miles_covered

    def randomAccident(self):
        r = randint(0, 5)
        if r == 0:
            return "You have a flat tire! Your car has stopped!"
        elif r == 1:
            return "Your car is having engine troubles! You've pulled over and must make repairs!"
        elif r == 2:
            return "Your windshield has a crack in it! You can't see so you have pulled over!"
        elif r == 3:
            return "You...uh...ran out of wiper fluid? YEAH you ran out of wiper fluid! Its always raining in Miami," \
                   "so...uh...get more of it, I guess?"
        else:
            return "DEAR GOD A MAN HAS FLUNG HIMSELF ONTO YOUR CAR! He somehow seems okay...and runs off. That was" \
                   "weird...Well now your car has damage on the hood not making it street legal. Repair it!"

    def issueRandom(self):
        if randint(0, 120) is 0:
            self.setCondition(-self.getCondition())
            return self.randomAccident()
        else:
            return "You keep chugging along..."

    def is_dead(self):
        if self._health == 0:
            return True 
        else:
            return False
