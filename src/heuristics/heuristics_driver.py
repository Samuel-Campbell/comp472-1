from game_builder.difficulty.game_difficulty import GameDifficultyEnum
from heuristics.random_search import random_search_driver
from heuristics.depth_first_search import depth_first_search_driver
from util.file import File


def random_search():
    random_search_driver.run(GameDifficultyEnum.NOVICE, 'novice_data.bin', 5000, 1000, 35)
    # random_search(GameDifficultyEnum.APPRENTICE, 'apprentice_random.bin', 100, 500)
    # random_search(GameDifficultyEnum.EXPERT, 'expert_random.bin', 100, 1000)
    # random_search(GameDifficultyEnum.MASTER, 'master_random.bin', 100, 2000)


def depth_first_search():
    model = File.load_binary('novice_data.bin')
    depth_first_search_driver.run(model, GameDifficultyEnum.NOVICE, 'novice_data.bin', 5000)

    # model = File.load_binary('apprentice_random.bin')
    # depth_first_search_driver.run(model, GameDifficultyEnum.APPRENTICE, 'apprentice_dfs.bin', 5000)

    # model = File.load_binary('expert_random.bin')
    # depth_first_search_driver.run(model, GameDifficultyEnum.EXPERT, 'expert_dfs.bin', 5000)

    # model = File.load_binary('master_random.bin')
    # depth_first_search_driver.run(model, GameDifficultyEnum.MASTER, 'master_dfs.bin', 5000)

if __name__ == '__main__':
    #random_search()
    depth_first_search()