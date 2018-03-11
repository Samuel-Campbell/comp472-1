from heuristics.strategic_solver.row_solver.bottom_row_solver import BottomRowSolver
from heuristics.strategic_solver.row_solver.top_row_solver import TopRowSolver
import os
import time


class StrategicSolver:
    def __init__(self, board, verbose=False, output=False):
        self.board = board
        self.verbose = verbose
        self.nb_moves = 0
        self.moves = []

    def solve(self):
        """
        1) solve top row
        2) solve bottom row
        :return: None
        """
        start = time.time()
        ts = TopRowSolver(self.board, verbose=self.verbose)
        ts.solve()
        self.nb_moves += ts.nb_moves
        self.moves += ts.move
        bs = BottomRowSolver(self.board, verbose=self.verbose)
        bs.solve()
        self.nb_moves += bs.nb_moves
        self.moves += bs.move
        end = time.time()
        self.save_output(self.moves, (end - start))

    def save_output(self, moves, time):
        root_directory = os.path.abspath(__file__ + "r/../../../")
        rel_dir = r'data/output/output.txt'
        filename = os.path.join(root_directory, rel_dir)
        file = open(filename, 'a')
        for m in moves:
            file.write(m)
        file.write('\n')
        file.write("{0:.5f}".format(time) + ' ms')
        file.write('\n')
        file.close()