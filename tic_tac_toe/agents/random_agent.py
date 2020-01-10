import random
import time

from .base_agent import Agent


class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)
        self._states_visited = 0

    def next_move(self, board):
        start = time.clock()
        
        valid_moves = self._valid_moves(board)
        move = random.choice(valid_moves)
        
        end = time.clock()

        self._time += (end-start)
        self._num_moves += 1
        return move
