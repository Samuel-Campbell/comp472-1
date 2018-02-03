from random import randint
import numpy

class DepthFirstSearch:
    clf = None

    move_to_int = {
        'u': 0,
        'd': 1,
        'r': 2,
        'l': 3
    }

    def __init__(self, board, max_iter=1000):
        """
        Constructor
        :param board: game_builder.board.game_board.GameBoard()
        :param max_iter: maximum depth of the DFS
        """
        self.board = board
        self.max_iter = max_iter
        self.permutation = []
        self.full_depth = 0
        self.board_states = {}

    def search(self, depth=0):
        """

        1) if max iteration is reached return False
        2) if game is cleared return True
        3) If game state already seen then return False (redundant movements)
        4) increment depth
        5) find best moves in order and sort them
        6) 10% of the time randomize the best moves to add an element of randomness
        7) Perform recursion

        :param depth: depth of the search
        :return: Boolean
        """
        if depth >= self.max_iter:
            return False
        if self.board.game_cleared():
            self.full_depth = depth
            return True

        game_state = self.board.get_board_state().copy()

        if str(game_state) in self.board_states:
            return False
        self.board_states[str(game_state)] = ''
        
        depth += 1
        probabilities = DepthFirstSearch.clf.predict_probabilities(game_state)
        rnd = randint(1, 10)
        if rnd == 1:
            numpy.random.shuffle(probabilities)
            first_best = probabilities.pop()[1]
            second_best = probabilities.pop()[1]
            third_best = probabilities.pop()[1]
            fourth_best = probabilities.pop()[1]

        else:
            probabilities.sort(key=lambda x: x[0])
            first_best = probabilities.pop()[1]
            second_best = probabilities.pop()[1]
            third_best = probabilities.pop()[1]
            fourth_best = probabilities.pop()[1]

        self.move(first_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[first_best], self.full_depth - depth + 1])
            return True
        self.undo_move(first_best)

        self.move(second_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[second_best], self.full_depth - depth + 1])
            return True
        self.undo_move(second_best)

        self.move(third_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[third_best], self.full_depth - depth + 1])
            return True
        self.undo_move(third_best)

        self.move(fourth_best)
        if self.search(depth):
            self.permutation.append(
                [game_state, self.move_to_int[fourth_best], self.full_depth - depth + 1])
            return True
        self.undo_move(fourth_best)

        return False

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