from utils import *


class Box:
    def __init__(self, x: int, y: int):
        self.shooted = 0
        self.sprites = [SPRITES["fog"], SPRITES["water"]]
        self.x = x
        self.y = y

    def sprite(self, x=-1, y=-1, mode=PLAYER):
        return self.sprites[self.shooted]

    def shoot(self, x, y):
        if x != self.x or y != self.y or self.shooted != 0:
            return -1
        self.shooted = 1
        return 0