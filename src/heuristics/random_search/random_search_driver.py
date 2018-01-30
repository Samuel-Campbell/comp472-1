from sys import stdout
from util.file import File
from heuristics.random_search.random_search import RandomSearch
from game_builder.board.game_board import GameBoard


def run(difficulty, filename, nb_of_boards, nb_of_search, max_iter=1000):
    """
    Main method for the driver

    1) iterate all randomly generated boards
    2) for every board perform x permutations
    3) for every permutation save all game states to dictionary
    4) if a state already exists then only store the best one.
       the best state is defined by the one with the less amount of moves
       till the objective.
    5) save binary

    dict:{
        <string representation of state>: [<int representation of state>, <next best move>]
        board_state: [[1, 2, 3..,], 2]
    }

    :param difficulty: <int> level of difficulty 0 -3 where 3 is the hardest
    :param filename: <str> file of binary model
    :param nb_of_boards: <int> number of randomly generated boards to play
    :param nb_of_search: <int> number of permutations per board
    :param max_iter: <int> max number of moves to clear a board
    :return: None
    """
    best_search_dict = {}
    for i in range(nb_of_boards):
        board = GameBoard(verbose=False)
        board.create_random_game(difficulty)
        rs = RandomSearch(board, max_iter=max_iter)
        for j in range(nb_of_search):
            rs.search()
        permutation = rs.get_best_permutation()
        __save_best_result(permutation, best_search_dict)
        percent = (i / nb_of_boards) * 100
        stdout.write("\rProgress: %f " % percent)
        stdout.flush()
    File.save_binary(filename, best_search_dict)


def __save_best_result(permutation, best_search_dict):
    """
    Saves board states to the dictionary

    1) if the state already exists in the dict then save the best one
    2) the best state is defined by the one with the less amount of moves
       till the objective

    :param permutation: Game state --> np.array([])
    :param best_search_dict: dict
    :return: None
    """
    for result in permutation:
        key = str(result[0])
        if key in best_search_dict:
            current_val = best_search_dict[str(result[0])]
            if current_val[2] > result[2]:
                best_search_dict[str(result[0])] = result
        else:
            best_search_dict[str(result[0])] = result
