from Game import Game
from Human import Human
from Board import Board

dimension = (10, 10)
board1 = Board(dimension[0], dimension[1])
board2 = Board(dimension[0], dimension[1])

game = Game(Human(board1), Human(board2))
game.start()