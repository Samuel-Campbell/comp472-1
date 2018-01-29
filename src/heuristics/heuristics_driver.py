from heuristics.random_search.random_search import RandomSearch
from game_builder.board.game_board import GameBoard
from game_builder.difficulty.game_difficulty import GameDifficultyEnum


if __name__ == '__main__':
    board = GameBoard(verbose=False)
    board.create_random_game(GameDifficultyEnum.NOVICE)
    rs = RandomSearch(board, max_iter=1000)
    result = rs.search()
    print(result[0])
    print(len(result[1]))