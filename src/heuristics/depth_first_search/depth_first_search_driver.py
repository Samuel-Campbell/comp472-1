from heuristics.depth_first_search.depth_first_search import DepthFirstSearch
from game_builder.board.game_board import GameDifficultyEnum, GameBoard
from training.classifier.abstract_classifier import AbstractClassifier
from util.file import File
from sys import stdout


def run(difficulty, filename, nb_of_boards, prediction_model, maximum_steps=1):
    """
    1) Load data points
    2) Load the ML model
    3) perform DFS
    4) if a search is successful then save it in the dictionary
    5) once all points are collected then overwrite old model with new one

    :param difficulty: difficulty level [0, 3] where 3 is the hardest
    :param filename: Name of data point dictionary file
    :param nb_of_boards: Number of random boards to generate
    :param prediction_model: Prediction model to use (based on difficulty)
    :param maximum_steps: Maximum amount of steps before failure
    :return: None
    """
    data = File.load_binary(filename)
    if data is None:
        data = {}
    prediction_model = File.load_binary(prediction_model)
    DepthFirstSearch.clf = AbstractClassifier(None)
    DepthFirstSearch.clf.model = prediction_model
    print('Max steps: {}'.format(str(maximum_steps)))
    best_search_dict = data
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
    return maximum_steps


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
