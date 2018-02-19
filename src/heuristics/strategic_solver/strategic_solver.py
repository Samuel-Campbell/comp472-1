from heuristics.strategic_solver.bottom_row_solver import BottomRowSolver
from heuristics.strategic_solver.top_row_solver import TopRowSolver


class StrategicSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        ts = TopRowSolver(self.board)
        ts.solve()
        bs = BottomRowSolver(self.board)
        bs.solve()