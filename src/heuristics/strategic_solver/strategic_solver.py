from heuristics.strategic_solver.row_solver.bottom_row_solver import BottomRowSolver
from heuristics.strategic_solver.row_solver.top_row_solver import TopRowSolver


class StrategicSolver:
    def __init__(self, board, verbose=False, output=False):
        self.board = board
        self.verbose = verbose
        self.nb_moves = 0

    def solve(self):
        """
        1) solve top row
        2) solve bottom row
        :return: None
        """
        ts = TopRowSolver(self.board, verbose=self.verbose)
        ts.solve()
        self.nb_moves += ts.nb_moves
        bs = BottomRowSolver(self.board, verbose=self.verbose)
        bs.solve()
        self.nb_moves += bs.nb_moves
