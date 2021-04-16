from Board import Board

class Player:
    def __init__(self, board : Board):
        self.board = board
        self.name = ""

    def playMove(self):
        pass

    def placeBoat(self):
        pass

    def placeBoats(self, boats):
        for boat in boats:
            self.placeBoat(boat)

    def getBoard(self):
        return self.board