from utils import *
from Player import Player
from Board import Board


class Human(Player):
    def __init__(self, board : Board):
        super().__init__(board)
        self.enterName()

    def enterName(self):
        self.name = input("Please enter your name Admiral :")

    def playMove(self, enemy: Player):
        print("Admiral " + self.name + " it's your turn to shoot !")
        valid = False
        coord = ["-1", "-1"]
        x = -1
        y = -1
        while not valid:
            strXY = input("Choose a box and enter the column and row :")
            coord = strXY.split()
            if len(coord) == 2:
                x = int(coord[0])
                y = int(coord[1])
                if x < 0 or x >= enemy.board.getWidth():
                    print("Please don't shoot outside the board !")
                    continue
                if y < 0 or y >= enemy.board.getHeight():
                    print("Please don't shoot outside the board !")
                    continue
                valid = True
            else:
                print("Please enter a column and a row like this : x y <return>")

        result = enemy.getBoard().shoot(x, y)
        if(result == -1):
            print("You already tried there !")
        elif(result == 0):
            print("Nothing there !")
        elif(result == 1):
            print("You hit Admiral !")


    def placeBoat(self, length):
        valid = False
        while not valid:
            print("Next boat to place : " + str(length) + " box long")
            strOrder = input("Admiral " + self.name + " please choose where to place your ship : enter a column, a row and a direction (L(eft), U(p), R(ight), D(own))")
            order = strOrder.split()
            if len(order) < 3:
                print("Wrong command Admiral !")
                continue
            x = int(order[0])
            y = int(order[1])

            direction = -1
            if order[2][0] == "L":
                direction = LEFT
            elif order[2][0] == "U":
                direction = UP
            elif order[2][0] == "R":
                direction = RIGHT
            elif order[2][0] == "D":
                direction = DOWN

            placed = self.board.placeBoat(x, y, length, direction)
            if placed < 0:
                print("No place here for your ship !")
            else:
                valid = True
