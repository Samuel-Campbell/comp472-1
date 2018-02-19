class PlayModeEnum:
    MANUAL = 'm'
    AUTO = 'a'


class GameMode:
    __play_mode = None

    def __init__(self):
        pass

    @staticmethod
    def run():
        """
        Obtain game mode from the user's inputs

        1) Ask user to enter a game mode
        2) While input is not valid then re-prompt user

        :return: PlayModeEnum --> MANUAL or AUTO
        """

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
        """
        Confirm whether a user's input is valid or not

        1) Iterate the PlayModeEnum list.
        2) if user's input corresponds to the enumerate variable then return true
        3) return false if no match were found

        :param input_str: string
        :return: boolean
        """

        if input_str.lower() == PlayModeEnum.MANUAL:
            GameMode.__play_mode = PlayModeEnum.MANUAL
            return True
        elif input_str.lower() == PlayModeEnum.AUTO:
            return True
        print('Your input is incorrect.')
        return False
