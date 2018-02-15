from game_builder.game_builder import GameBuilder
from training import training_driver
import sys


def play():
    """
    Main driver of the program
    1) Builds the game
    2) Runs the game
    3) Loops until user types anything other than 'y' or 'Y'
    :return: None
    """

    print('================================================')
    print('Welcome to Candy Crisis')
    print('================================================')
    while True:
        game = GameBuilder.build()
        print('------------------------------------------------')
        game.run()
        input_str = input('Do you want to keep playing? (y/Y)')
        if input_str.lower() == 'y':
            pass
        else:
            break
    print('Thanks for playing')


def train():
    training_driver.run()


if __name__ == '__main__':
    command = sys.argv[1]
    if command == 'train':
        train()
    elif command == 'play':
        play()
    else:
        print('Argument {} not recognized'.format(command))