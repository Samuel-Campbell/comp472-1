from game_builder.game.abstract_game import AbstractGame
from heuristics.best_first_search.best_first_search import BestFirstSearch


class AutoGame(AbstractGame):
    def __init__(self, board):
        AbstractGame.__init__(self, board)

    def run(self):
        bfs = BestFirstSearch(self._board)
        bfs.search()
