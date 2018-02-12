class ProbabilisticSearch:
    clf = None

    def __init__(self, board):
        self.board_states = {}
        self.board = board
        self.move_sequence = []

    def new_game_state(self, game_state):
        if str(game_state) in self.board_states:
            return False
        self.board_states[str(game_state)] = ''
        return True

    def correct_move(self, probabilities, game_state):
        self.move(probabilities)
        if self.new_game_state(game_state):
            return True
        else:
            self.undo_move(probabilities)
        return False

    def search(self):
        while not(self.board.game_cleared()):
            game_state = self.board.get_board_state().copy()
            probabilities = ProbabilisticSearch.clf.predict_probabilities(game_state)
            probabilities.sort(key=lambda x: x[0])

            if self.correct_move(probabilities[3][1], game_state):
                pass
            elif self.correct_move(probabilities[2][1], game_state):
                pass
            elif self.correct_move(probabilities[1][1], game_state):
                pass
            elif self.correct_move(probabilities[0][1], game_state):
                pass
            else:
                return False
        return True

    def move(self, input_str):
        """
        move
        :param input_str: string
        :return: None
        """
        if input_str == 'u':
            self.board.move_up()
        elif input_str == 'd':
            self.board.move_down()
        elif input_str == 'l':
            self.board.move_left()
        elif input_str == 'r':
            self.board.move_right()

    def undo_move(self, input_str):
        """
        Undo a move
        :param input_str: string
        :return: None
        """
        if input_str == 'u':
            self.board.move_down()
        elif input_str == 'd':
            self.board.move_up()
        elif input_str == 'l':
            self.board.move_right()
        elif input_str == 'r':
            self.board.move_left()