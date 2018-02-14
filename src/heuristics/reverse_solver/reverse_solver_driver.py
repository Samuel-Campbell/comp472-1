from heuristics.reverse_solver.reverse_solver import ReverseSolver
from util.file import File
from sys import stdout


def run(dataset, steps, difficulty, nb_configurations):
    best_search_dict = File.load_binary(dataset)
    if best_search_dict is None:
        best_search_dict = {}
    for i in range(nb_configurations):
        rs = ReverseSolver(steps)
        rs.set_difficulty(difficulty)
        rs.solve()
        __save_best_result(rs.solutions, best_search_dict)
        percent = (i / nb_configurations) * 100
        stdout.write("\rProgress: %f " % percent)
        stdout.flush()
    print()
    File.save_binary(dataset, best_search_dict)


def __save_best_result(solutions, best_search_dict):
    """
    Saves board states to the dictionary

    1) if the state already exists in the dict then save the best one
    2) the best state is defined by the one with the less amount of moves
       till the objective

    :param permutation: Game state --> np.array([])
    :param best_search_dict: dict
    :return: None
    """
    for key in solutions:
        value = solutions[key]
        if key in best_search_dict:
            pass
        elif not(value == ''):
            best_search_dict[key] = value
