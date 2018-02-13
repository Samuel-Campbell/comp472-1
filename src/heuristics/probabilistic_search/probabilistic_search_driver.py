from util.file import File
from heuristics.probabilistic_search.probabilistic_search import ProbabilisticSearch
from training.classifier.abstract_classifier import AbstractClassifier
from game_builder.board.game_board import GameBoard, GameDifficultyEnum
import time


def run(difficulty):
    board = GameBoard(verbose=False)
    board.create_random_game(difficulty)
    dfs = ProbabilisticSearch(board)
    dfs.search()
    print(len(dfs.move_sequence))


if __name__ == '__main__':
    prediction_model = File.load_binary('novice_model.bin')
    ProbabilisticSearch.clf = AbstractClassifier(None)
    ProbabilisticSearch.clf.model = prediction_model
    start = time.time()
    for i in range(5):
        run(GameDifficultyEnum.NOVICE)
    end = time.time()
    print(end - start)