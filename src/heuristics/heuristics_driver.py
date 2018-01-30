from heuristics.random_search.random_search import RandomSearch
from game_builder.board.game_board import GameBoard
from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from sys import stdout
from util.file import File


def random_search(difficulty, filename, nb_of_boards, nb_of_search, max_iter=1000):
    best_search_dict = {}
    for i in range(nb_of_boards):
        board = GameBoard(verbose=False)
        board.create_random_game(difficulty)
        rs = RandomSearch(board, max_iter=max_iter)
        for j in range(nb_of_search):
            rs.search(str(j))
        permutation = rs.get_best_permutation()
        save_best_result(permutation, best_search_dict)
        percent = (i / nb_of_boards) * 100
        stdout.write("\rProgress: %f " % percent)
        stdout.flush()
    File.save_binary(filename, best_search_dict)


def save_best_result(permutation, best_search_dict):
    for result in permutation:
        key = str(result[0])
        if key in best_search_dict:
            current_val = best_search_dict[str(result[0])]
            if current_val[2] > result[2]:
                best_search_dict[str(result[0])] = result
        else:
            best_search_dict[str(result[0])] = result


if __name__ == '__main__':
    random_search(GameDifficultyEnum.NOVICE, 'novice_random.bin', 5000, 1000, 35)
    #random_search(GameDifficultyEnum.APPRENTICE, 'apprentice_random.bin', 100, 500)
    #random_search(GameDifficultyEnum.EXPERT, 'expert_random.bin', 100, 1000)
    #random_search(GameDifficultyEnum.MASTER, 'master_random.bin', 100, 2000)