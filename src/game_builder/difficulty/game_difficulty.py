class GameDifficultyEnum:
    NOVICE = '0'
    APPRENTICE = '1'
    EXPERT = '2'
    MASTER = '3'
    MODES = [NOVICE, APPRENTICE, EXPERT, MASTER]


class GameDifficulty:
    play_difficulty = None

    @staticmethod
    def run():
        while True:
            print('\nPlease enter a difficulty:')
            print('Novice: 0')
            print('Apprentice: 1')
            print('Expert: 2')
            print('Master: 3')
            play_mode = input()
            if GameDifficulty.__validate_input(play_mode):
                break
        return GameDifficulty.play_difficulty

    @staticmethod
    def __validate_input(input_str):
        for variable in GameDifficultyEnum.MODES:
            if input_str.lower() == variable:
                GameDifficulty.play_difficulty = variable
                return True
        print('Your input is incorrect.')
        return False
