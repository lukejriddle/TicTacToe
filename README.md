# Tic-Tac-Toe AI
An adversarial search agent for a simple game for tic-tac-toe.

*The base Tic-Tac-Toe game was written and created by Stefan Saftescu, whose Github can be found [here](https://github.com/SliMM).*

To run, run main.py. The game allows for the selection of each players' agent, be it human (0 - console input agent), random, or a search agent.

## The AI
The AI for the game uses minimax adversarial search to find the optimal move given the state of the board. This is trivial for boards of size 3x3, so solutions are found instantly at such a size. This agent is designed to be able to scale up larger board sizes, 20x20 and up. In order to be able to achieve this, a few heurstics were incorporated:

### Alpha-Beta Pruning
Read more [here](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

### Zobrist Hashing
Read more [here](https://en.wikipedia.org/wiki/Zobrist_hashing).

### Board State Analysis
The *heuristic* method of class Board assigns a value to a given board state based on the number of Xs and Os on the board in addition to the existing lines of Xs and Os that might indicate one player is closer to winning than another. Exact values are a result of trial-and-error. Heuristic values for each state are stored in additional cache in so that they needn't be calculated again.
