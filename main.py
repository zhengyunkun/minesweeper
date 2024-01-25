from game import Game 
# Import the Game class from game.py
from board import Board
# Import the Board class from board.py

size = (16, 30)
prob = 0.3
board = Board(size, prob)
screenSize = (900, 500)
game = Game(board, screenSize)
game.run()