from random import randint


# class to generate random encounters at various points in game
class RandomEncounter:
    def __init__(self):
        self._goodlocals = ['gas station', 'Sublix', 'rest stop']
        self._badlocals = ['swamp', 'ghost town', 'traffic jam']
        self._people = ['tourists', 'swamp men', 'senior citizen']


