from game_builder.game.abstract_game import AbstractGame
from heuristics.strategic_solver.strategic_solver import StrategicSolver


class AutoGame(AbstractGame):
<<<<<<< HEAD
=======
    move_to_int = {
        0: 'w',
        1: 's',
        2: 'd',
        3: 'a'
    }

>>>>>>> 3ebc82fae5b961daf22b027b9fa49bf18db53f18
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        ss = StrategicSolver(self._board, verbose=True)
        ss.solve()
        print('Game Cleared Automatically in {} steps'.format(ss.nb_moves))
