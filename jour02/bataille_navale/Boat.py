from utils import *
from Box import Box


class Boat(Box):
    def __init__(self, boxes):
        self.parts = {}
        for box in boxes:
            self.parts[(box[0], box[1])] = False
        self.sprites = {(False, False): SPRITES["part"],
                        (True, False): SPRITES["hit"],
                        (True, True): SPRITES["sunk"]}
        self.sunk = False

    def shoot(self, x, y):
        if (x, y) in self.parts:
            if self.parts[(x, y)]:
                return -1
            self.parts[(x, y)] = True

            self.updateSunk()
            return 1
        return 0

    def sprite(self, x, y, mode=PLAYER):
        if (x, y) in self.parts:
            if mode == ENEMY and not self.parts[(x, y)] and not self.sunk:
                return SPRITES["fog"]

            return self.sprites[(self.parts[(x, y)], self.sunk)]

    def updateSunk(self):
        for hit in self.parts.values():
            if not hit:
                return
        self.sunk = True
