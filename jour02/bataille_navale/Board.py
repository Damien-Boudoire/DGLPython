from utils import *
from Box import Box
from Boat import Boat


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.boats = []

        self.boxes = []
        for i in range(0, self.width):
            self.boxes.append([])
            for j in range(0, self.height):
                self.boxes[i].append(Box(i, j))

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getBox(self, x, y):
        return self.boxes[x][y]

    def placeBoat(self, x, y, length, orientation):
        if orientation == LEFT and x - (length-1) < 0:
            return -1
        if orientation == RIGHT and x + (length-1) >= self.width:
            return -1
        if orientation == UP and y - (length-1) < 0:
            return -1
        if orientation == DOWN and y + (length-1) >= self.height:
            return -1

        for i in range(0, length):
            if orientation == LEFT and isinstance(self.boxes[x-i][y], Boat):
                return -1
            if orientation == RIGHT and isinstance(self.boxes[x + i][y], Boat):
                return -1
            if orientation == UP and isinstance(self.boxes[x][y - i], Boat):
                return -1
            if orientation == DOWN and isinstance(self.boxes[x][y + i], Boat):
                return -1

        boxes = []
        for i in range(0, length):
            if orientation == LEFT:
                boxes.append((x-i, y))
            if orientation == RIGHT:
                boxes.append((x + i, y))
            if orientation == UP:
                boxes.append((x, y - i))
            if orientation == DOWN:
                boxes.append((x, y + i))

        boat = Boat(boxes)
        for box in boxes:
            self.boxes[box[0]][box[1]] = boat

        self.boats.append(boat)
        return 1

    def shoot(self, x, y):
        return self.boxes[x][y].shoot(x, y)

    def endGame(self):
        for boat in self.boats:
            if not boat.sunk:
                return False
        return True

    def getSprite(self, x, y, mode = PLAYER):
        return self.boxes[x][y].sprite(x, y, mode)
