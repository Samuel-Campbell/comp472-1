from game_builder.game_builder import GameBuilder

if __name__ == '__main__':
    print('================================================')
    print('Welcome to Candy Crisis')
    print('================================================')
    game = GameBuilder.build()
    print('------------------------------------------------')
    game.display()