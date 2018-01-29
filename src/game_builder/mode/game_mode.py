class PlayModeEnum:
    MANUAL = 'm'
    AUTO = 'a'


class GameMode:
    __play_mode = None

    def __init__(self):
        pass

    @staticmethod
    def run():
        while True:
            print('\nPlease enter a game mode:')
            print('Manual: m/M')
            print('Auto: a/A')
            play_mode = input()
            if GameMode.__validate_input(play_mode):
                break
        return GameMode.__play_mode

    @staticmethod
    def __validate_input(input_str):
        if input_str.lower() == PlayModeEnum.MANUAL:
            GameMode.__play_mode = PlayModeEnum.MANUAL
            return True
        elif input_str.lower() == PlayModeEnum.AUTO:
            print('Game mode not yet supported.')
            return False
        print('Your input is incorrect.')
        return False
