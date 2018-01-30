from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from heuristics.random_search import random_search_driver


def random_search():
    random_search_driver.run(GameDifficultyEnum.NOVICE, 'novice_random.bin', 5000, 1000, 35)
    # random_search(GameDifficultyEnum.APPRENTICE, 'apprentice_random.bin', 100, 500)
    # random_search(GameDifficultyEnum.EXPERT, 'expert_random.bin', 100, 1000)
    # random_search(GameDifficultyEnum.MASTER, 'master_random.bin', 100, 2000)


def intuitive_search():
    pass


if __name__ == '__main__':
    random_search()