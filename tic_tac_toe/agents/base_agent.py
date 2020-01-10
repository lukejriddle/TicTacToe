from abc import ABC, abstractmethod
from collections import namedtuple

from ..board import CellState
from ..player import PLAYER_NAMES


class Move(namedtuple("Move", ["player", "row", "col"])):
    def __repr__(self):
        return "Move(player={},row={},col={})".format(
            PLAYER_NAMES[self.player], self.row, self.col)


class Agent(ABC):

    def __init__(self, player):
        self._player = player
        self._num_moves = 0
        self._time = 0
        self._states_visted = 0

    @abstractmethod
    def next_move(self, board):
        pass

    def _valid_moves(self, board):
        valid_moves = []
        for i, j in board.empty_cells:
            valid_moves.append(Move(self._player, i, j))

        return valid_moves

    @property
    def average_runtime(self):
        if self._num_moves == 0:
            return 0

        return self._time / self._num_moves

    @property
    def states_visited(self):
        return self._states_visited
