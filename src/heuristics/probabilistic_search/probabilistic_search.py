import numpy


class ProbabilisticSearch:
    novice_goal_state = [1, 2, 2, 1, 1, 0, 3, 2, 3, 2, 1, 2, 2, 1, 1]
    clf = None

    def __init__(self, board):
        self.board_states = {}
        self.board = board
        self.move_sequence = []

    def next_move(self, game_state):
        if str(game_state) in self.board_states:
            try:
                self.board_states[str(game_state)].pop()
            except IndexError:
                pass
        else:
            sub_arr = numpy.subtract(numpy.array(game_state), numpy.array(ProbabilisticSearch.novice_goal_state))
            move_prob = ProbabilisticSearch.clf.predict_probabilities(sub_arr)
            move_prob.sort(key=lambda x: x[0])
            self.board_states[str(game_state)] = move_prob
        return self.board_states[str(game_state)]

    def search(self):
        while not(self.board.game_cleared()):
            game_state = self.board.get_board_state().copy()
            next_move = self.next_move(game_state)

            # All moves given a board state have been exhausted
            if len(next_move) == 0:
                self.undo_move(self.move_sequence.pop())

            # The best move leads to nowhere
            elif len(next_move) < 4:
                self.undo_move(self.move_sequence.pop())
                self.move(next_move[len(next_move) - 1][1])
                self.move_sequence.append(next_move[len(next_move) - 1][1])

            # The best move
            else:
                self.move(next_move[len(next_move) - 1][1])
                self.move_sequence.append(next_move[len(next_move) - 1][1])

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