from util.file import File
from game_builder.board.game_board import GameBoard
import time
import numpy


def metrics(arr):
    ones = [1 if x == 1 else 0 if x == 0 else -1 for x in arr]
    twos = [1 if x == 2 else 0 if x == 0 else -1 for x in arr]
    threes = [1 if x == 3 else 0 if x == 0 else -1 for x in arr]
    fours = [1 if x == 4 else 0 if x == 0 else -1 for x in arr]
    fives = [1 if x == 5 else 0 if x == 0 else -1 for x in arr]
    sixes = [1 if x == 6 else 0 if x == 0 else -1 for x in arr]

    m1 = pattern_dictionary[str(ones)]['steps']
    m2 = pattern_dictionary[str(twos)]['steps']
    m3 = pattern_dictionary[str(threes)]['steps']

    try:
        m4 = pattern_dictionary[str(fours)]['steps']
    except:
        m4 = 0

    try:
        m5 = pattern_dictionary[str(fives)]['steps']
    except:
        m5 = 0

    try:
        m6 = pattern_dictionary[str(sixes)]['steps']
    except:
        m6 = 0

    return m1 + m2 + m3 + m4 + m5 + m6

pattern_dictionary = File.load_binary('pattern_dictionary.bin')
#arr = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3]
arr = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
lst = []
start = time.time()
for i in range(1):
    numpy.random.shuffle(arr)
    board = GameBoard(verbose=False)
    board.create_game_from_array(arr)

    closed_states = {}
    moves = 0
    board.display()
    while not board.game_cleared():
        right = 5000
        left = 5000
        up = 5000
        down = 5000

        closed_states[str(board.get_board_state())] = 1

        if board.move_right():
            state = board.get_board_state()
            if str(state) not in closed_states:
                right = metrics(state)
            board.move_left()

        if board.move_down():
            state = board.get_board_state()
            if str(state) not in closed_states:
                down = metrics(state)
            board.move_up()

        if board.move_left():
            state = board.get_board_state()
            if str(state) not in closed_states:
                left = metrics(state)
            board.move_right()

        if board.move_up():
            state = board.get_board_state()
            if str(state) not in closed_states:
                up = metrics(state)
            board.move_down()

        movement = min([up, down, left, right])
        lst.append(movement)
        if movement == up:
            board.move_up()
        elif movement == down:
            board.move_down()
        elif movement == right:
            board.move_right()
        elif movement == left:
            board.move_left()

        moves += 1

    print('Completed in {} moves'.format(moves))
end = time.time()
print('{} ms'.format(end - start))
print(lst)