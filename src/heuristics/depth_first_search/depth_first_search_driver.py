from heuristics.depth_first_search.depth_first_search import DepthFirstSearch
from game_builder.board.game_board import GameDifficultyEnum, GameBoard
from training.classifier.abstract_classifier import AbstractClassifier
from util.file import File
from sys import stdout


def run(model, difficulty, filename, nb_of_boards):
    maximum_steps = 1
    DepthFirstSearch.clf = AbstractClassifier(None)
    print('Max steps: {}'.format(str(maximum_steps)))
    best_search_dict = model
    for i in range(nb_of_boards):
        board = GameBoard(verbose=False)
        board.create_random_game(difficulty)
        dfs = DepthFirstSearch(board, max_iter=maximum_steps)
        result = dfs.search()
        if result:
            __save_best_result(dfs.permutation, best_search_dict)
            percent = (i / nb_of_boards) * 100
            stdout.write("\rProgress: %f " % percent)
            stdout.flush()
        else:
            maximum_steps += 1
            print('Maximum steps increased to {}'.format(str(maximum_steps)))
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
            if current_val[2] >= result[2]:
                best_search_dict[str(result[0])] = result
        else:
            best_search_dict[str(result[0])] = result
