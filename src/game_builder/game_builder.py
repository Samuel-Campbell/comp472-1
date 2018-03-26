from game_builder.mode.game_mode import GameMode, PlayModeEnum
from game_builder.board.game_board import GameBoard
from game_builder.game.manual_game import ManualGame
from game_builder.game.auto_game import AutoGame
import os
import time


class GameBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build():
        """
        Builder pattern
        1) Ask user for game mode
        2) Ask user for game difficulty
        3) If mode set to manual then create a random board
        4) if mode set to auto then use ML model to solve puzzle
        :return: None
        """

        mode = GameMode.run()

        root_directory = os.path.abspath(__file__ + "r/../../")
        rel_path = r'data/game/'
        directory_path = os.path.join(root_directory, rel_path)

        input1 = GameBoard.obtain_game_from_file(directory_path + 'input1.txt')
        input2 = GameBoard.obtain_game_from_file(directory_path + 'input2.txt')
        input3 = GameBoard.obtain_game_from_file(directory_path + 'input3.txt')
        input4 = GameBoard.obtain_game_from_file(directory_path + 'input4.txt')

        if mode == PlayModeEnum.MANUAL:
            for game in input1:
                board = GameBoard()
                board.create_game_from_array(game)
                print('------------------------------------------------')
                game = ManualGame(board)
                game.run()
        else:
            for game in input1:
                board = GameBoard(verbose=False)
                board.create_game_from_array(game)
                game = AutoGame(board)
                start = time.time()
                game.run()
                end = time.time()
                GameBuilder.save('output1.txt', board.move_sequence, end - start)

            for game in input2:
                board = GameBoard(verbose=False)
                board.create_game_from_array(game)
                game = AutoGame(board)
                start = time.time()
                game.run()
                end = time.time()
                GameBuilder.save('output2.txt', board.move_sequence, end - start)

            for game in input3:
                board = GameBoard(verbose=False)
                board.create_game_from_array(game)
                game = AutoGame(board)
                start = time.time()
                game.run()
                end = time.time()
                GameBuilder.save('output3.txt', board.move_sequence, end - start)

            for game in input4:
                board = GameBoard(verbose=False)
                board.create_game_from_array(game)
                game = AutoGame(board)
                start = time.time()
                game.run()
                end = time.time()
                GameBuilder.save('output4.txt', board.move_sequence, end - start)
        print('Solved all games')

    @staticmethod
    def save(filename, move_sequence, time_span):
        root_directory = os.path.abspath(__file__ + "r/../../")
        rel_dir = r'data/output/' + filename
        filename = os.path.join(root_directory, rel_dir)
        file = open(filename, 'a')
        for m in move_sequence:
            file.write(m)
        file.write('\n')
        file.write("{0:.6f}".format(time_span) + ' ms')
        file.write('\n')
        file.close()