from game_builder.game.abstract_game import AbstractGame
from heuristics.strategic_solver.strategic_solver import StrategicSolver


class AutoGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        ss = StrategicSolver(self._board, verbose=True)
        ss.solve()
