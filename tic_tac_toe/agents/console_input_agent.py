from .base_agent import Agent, Move
from ..player import PLAYER_NAMES

import time


class ConsoleInputAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        def _input_move():
            try:
                print("")
                print("{}'s next move".format(PLAYER_NAMES[self._player]))
                row = int(input("\trow: "))
                col = int(input("\tcol: "))
                print("")

                return Move(self._player, row, col)
            except ValueError:
                print("Row an col must be integers between 0 and {}".format(
                    board.size))

        start = time.clock()
        move = _input_move()
        valid_moves = self._valid_moves(board)

        while move not in valid_moves:
            print("{} is not valid, try again.".format(move))
            print("Valid moves: " + str(valid_moves))
            move = _input_move()

        end = time.clock()
        
        self._time += (end-start)
        self._num_moves += 1

        return move
