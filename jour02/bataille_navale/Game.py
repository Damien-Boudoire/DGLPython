from utils import *
from Player import Player
from Human import Human
from Board import Board


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.boats = [5, 4, 3, 3, 2]
        self.players = (player1, player2)

    def start(self):
        self.placeBoats()

        currentPlayer = 0
        opponent = 1
        while(not self.players[0].getBoard().endGame() and
              not self.players[1].getBoard().endGame()):

            self.printBoards(self.players[currentPlayer].getBoard(), self.players[opponent].getBoard())
            self.players[currentPlayer].playMove(self.players[opponent])
            self.clearScreen()

            currentPlayer = (currentPlayer + 1) % 2
            opponent = (opponent + 1) % 2



    def placeBoats(self):
        if isinstance(self.players[0], Human):
            print("Admiral " + self.players[0].name +" it's your turn to place your fleet.")
        for boat in self.boats:
            self.printBoard(self.players[0].getBoard())
            self.players[0].placeBoat(boat)
        self.printBoard(self.players[0].getBoard())

        self.clearScreen()

        if isinstance(self.players[1], Human):
            print("Admiral " + self.players[1].name +" it's your turn to place your fleet.")
        for boat in self.boats:
            self.printBoard(self.players[1].getBoard())
            self.players[1].placeBoat(boat)
        self.printBoard(self.players[1].getBoard())

        self.clearScreen()

        for i in range(0,10):
            print("")

    def playMove(self, player):
        player.playMove()

    def drawBoard(self, board: Board, mode=PLAYER):
        lines = []
        for y in range(0, board.getHeight()):
            line = ""
            for x in range(0, board.getWidth()):
                line += board.getSprite(x, y, mode)
            lines.append(line)
        return lines

    def printBoard(self, board: Board, mode=PLAYER):
        lines = self.drawBoard(board, mode)
        for line in lines:
            print(line)

    def printBoards(self, playerBoard, enemyBoard):
        playerScreen = self.drawBoard(playerBoard, PLAYER)
        enemyScreen = self.drawBoard(enemyBoard, ENEMY)

        for i in range(0, len(playerScreen)):
            print(playerScreen[i] + " || " + enemyScreen[i])

    def clearScreen(self):
        input("It's your opponent turn, press enter and don't look the screen !")
        for i in range(0,15):
            print("")
        input("Press enter to start")