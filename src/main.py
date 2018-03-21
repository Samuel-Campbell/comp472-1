from game_builder.game_builder import GameBuilder


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
    GameBuilder.build()
    print('Thanks for playing')


if __name__ == '__main__':
    play()
