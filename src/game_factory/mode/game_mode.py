class PlayModeEnum:
    MANUAL = 'm'
    AUTO = 'a'
    MODES = [MANUAL, AUTO]


class GameMode:
    play_mode = None

    def __init__(self):
        pass

    @staticmethod
    def run():
        while True:
            print('\nPlease enter a game mode:')
            print('Manuel: m/M')
            print('Auto: a/A')
            play_mode = input()
            if GameMode.validate_input(play_mode):
                break

    @staticmethod
    def validate_input(input_str):
        for variable in PlayModeEnum.MODES:
            if input_str.lower() == variable:
                GameMode.play_mode = variable
                return True
        print('Your input is incorrect.')
        return False
