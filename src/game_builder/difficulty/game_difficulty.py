class GameDifficultyEnum:
    NOVICE = '0'
    APPRENTICE = '1'
    EXPERT = '2'
    MASTER = '3'
    MODES = [NOVICE, APPRENTICE, EXPERT, MASTER]


class GameDifficulty:
    __play_difficulty = None

    @staticmethod
    def run():
        """
        Sets the game's difficulty by prompting the user

        1) Validate for correct inputs
        2) While input is incorrect re-prompt user

        :return: GameDifficultyEnum
        """

        while True:
            print('\nPlease enter a difficulty:')
            print('Novice: 0')
            print('Apprentice: 1')
            print('Expert: 2')
            print('Master: 3')
            play_mode = input()
            if GameDifficulty.__validate_input(play_mode):
                break
        return GameDifficulty.__play_difficulty

    @staticmethod
    def __validate_input(input_str):
        """
        Validates the input string of the user

        1) Iterate GameDifficultyEnum list
        2) if iterated variable matches input_str then return True
        3) else return False if no matches are found

        :param input_str: string
        :return: boolean
        """

        for variable in GameDifficultyEnum.MODES:
            if input_str.lower() == variable:
                GameDifficulty.__play_difficulty = variable
                return True
        print('Your input is incorrect.')
        return False
