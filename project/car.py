# Escape to Miami


class Car:
    def __init__(self):
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

    def getFuel(self,):
        return self._fuel

    def setFuel(self, n):
        self._fuel += n

    def getCondition(self):
        return self._condition

    # when condition changes, car will slow down
    def setCondition(self, n):
        self._condition += n
        n *= 0.01
        self.updateSpeed(n)

    def updateSpeed(self, n):
        self._speed += n

    def getSpeed(self):
        return self._speed

    # position is purely based on speed
    def updatePosition(self):
        self._position = self._position + self.getSpeed()

    
