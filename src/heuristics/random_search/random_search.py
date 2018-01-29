from random import randint


class RandomSearch:
    def __init__(self, board, max_iter):
        self.board = board
        self.max_iter = max_iter

    def search(self):
        iteration = 0
        moves = []
        while iteration < self.max_iter:
            move = self.__randomize_move()
            moves.append([move, self.board.get_board_state()])
            iteration += 1
            if self.board.game_cleared():
                break
        if iteration < self.max_iter:
            return True, moves
        return False, moves

    def __randomize_move(self):
        move = randint(0, 3)
        if move == 0:
            self.board.move_up()
        elif move == 1:
            self.board.move_down()
        elif move == 2:
            self.board.move_right()
        elif move == 3:
            self.board.move_left()
        return move
