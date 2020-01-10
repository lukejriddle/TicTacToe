from tic_tac_toe.game import Player, Game
from tic_tac_toe.board import Board
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent
from tic_tac_toe.agents.dfs_agent import DFSAgent
from tic_tac_toe.agents.alphabeta_agent import AlphaBetaAgent

AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Random Agent", RandomAgent),
    ("DFS Agent", DFSAgent),
    ("Alpha-Beta Agent", AlphaBetaAgent)
]

RESULTS = [
    ["Draws", 0],
    ["X wins", 0],
    ["O wins", 0]
]


def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = "\n".join(
                map(lambda x: "\t{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: \n{}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent
        except ValueError:
            return None

    agent = _try_pick()

    while agent is None:
        print("Incorect selection, try again.")
        agent = _try_pick()

    return AGENTS[agent][1](player)


def main():
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)

    size = int(input("Select size of the board >= 3: "))

    print("Select number in a row to win, <=",size,": ", end = '')
    to_win = int(input(""))

    random_board = input("Random board state? y/[n]:")

    play = "y"
    games = 0

    while play == "y":
        if(random_board == "y"):
            game_board = Board(size, to_win)
            game_board.randomize()
            winner = game_board.winner
            while(winner is not None):
                game_board = Board(size, to_win)
                game_board.randomize()
                winner = game_board.winner
        else:
            game_board = None

        game = Game(player_x, player_o, size, to_win, game_board)
        res = game.play()
        games += 1
        
        RESULTS[res + 1][1] += 1

        for line in RESULTS:
            print(*line)

        print("")

        print("X average runtime: ",player_x.average_runtime)
        print("O average runtime: ",player_o.average_runtime)
        print("States visited X", player_x.states_visited)
        print("States visited O", player_o.states_visited)

        play = input("Play again? y/[n]: ")

    #exit = input("Finished")


if __name__ == "__main__":
    main()
