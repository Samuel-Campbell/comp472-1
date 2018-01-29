import numpy


class GameBoard:
    board = numpy.zeros(15)

    candy_dict = {
        'reese': 'r',
        'bazooka': 'b',
        'walnetto': 'w',
        'york_mini': 'y',
        'gobstopper': 'g',
        'pez': 'p'
    }