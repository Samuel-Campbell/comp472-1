from game_builder.game_builder import GameBuilder


def run():
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


if __name__ == '__main__':
    run()