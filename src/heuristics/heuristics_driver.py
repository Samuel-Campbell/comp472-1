from heuristics.random_search.random_search import RandomSearch
from game_builder.board.game_board import GameBoard
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from sys import stdout
from util.file import File


def random_search(difficulty, nb_of_boards, nb_of_search, max_iter=1000):
    best_search_dict = {}
    for i in range(nb_of_boards):
        board = GameBoard(verbose=False)
        board.create_random_game(difficulty)
        rs = RandomSearch(board, max_iter=max_iter)

        for j in range(nb_of_search):
            rs.search(str(j))

        best_search_dict[i] = rs.get_min()
        rs.reset()
        percent = (i / nb_of_boards) * 100
        stdout.write("\rProgress: %f " % percent)
        stdout.flush()
    File.save_binary('random_novice.bin', best_search_dict)


if __name__ == '__main__':
    random_search(GameDifficultyEnum.NOVICE, 500, 1000)