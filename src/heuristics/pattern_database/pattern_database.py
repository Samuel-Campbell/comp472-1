from itertools import permutations
from util.file import File
from sys import stdout


class PatternDatabase:
    def __init__(self):
        self.pattern_dictionary = {}

    def find_patterns(self):
        pattern_1 = list(set(permutations([0, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 5)))
        pattern_2 = list(set(permutations([0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, -1, -1, -1, -1], 5)))

        unsolved_dictionary = {}
        solved_dictionary = {}

        self.create_patterns(pattern_1, [1, 2, 0], unsolved_dictionary)
        self.create_patterns(pattern_2, [1, 0, 10], solved_dictionary)
        self.merge_patterns(solved_dictionary, unsolved_dictionary)

    def create_patterns(self, single_row_pattern, variable_count, dictionary):
        dual_row_pattern = []
        for i in range(len(single_row_pattern)):
            for j in range(len(single_row_pattern)):
                dual_row_pattern.append(single_row_pattern[i] + single_row_pattern[j])

        triple_row_pattern = []
        for i in range(len(single_row_pattern)):
            for j in range(len(dual_row_pattern)):
                triple_row_pattern.append(single_row_pattern[i] + dual_row_pattern[j])

        for i in range(len(triple_row_pattern)):
            count_0 = triple_row_pattern[i].count(0)
            count_1 = triple_row_pattern[i].count(1)
            count_2 = triple_row_pattern[i].count(2)
            if (count_1 == variable_count[1]) and (count_0 == variable_count[0]) and count_2 == variable_count[2]:
                dictionary[str(list(triple_row_pattern[i]))] = list(triple_row_pattern[i])

    def merge_patterns(self, solved_dictionary, unsolved_dictionary):
        x = 0
        for pattern_1 in unsolved_dictionary:
            percent = (x / len(unsolved_dictionary)) * 100
            stdout.write("\rProgress: %f " % percent)
            stdout.flush()
            array_1 = unsolved_dictionary[pattern_1]
            for pattern_2 in solved_dictionary:
                array_2 = solved_dictionary[pattern_2]

                # don't care about middle row
                array_2[5:10] = [0 if x == 0 else -1 for x in array_2[5:10]]

                # unsolved column replace with -1
                for i in range(len(array_2[:5])):
                    if (array_2[i] != 2) or (array_2[i + 10] != 2):
                        if array_2[i] != 0:
                            array_2[i] = -1

                        if array_2[i + 10] != 0:
                            array_2[i + 10] = -1

                # find collision between solved and unsolved
                ones = set([i for i, j in enumerate(array_1) if j == 1])
                twos = set([i for i, j in enumerate(array_2) if j == 2])
                intersection = ones.intersection(twos)

                if len(intersection) > 0:
                    continue

                # make sure zeros are at the same index
                zero_1 = [i for i, j in enumerate(array_1) if j == 0]
                zero_2 = [i for i, j in enumerate(array_2) if j == 0]

                if not(zero_1 == zero_2):
                    continue

                # merge arrays
                final_board = []
                for i in range(len(array_1)):
                    if array_2[i] == 2:
                        final_board.append(2)
                    else:
                        final_board.append(array_1[i])

                self.pattern_dictionary[str(final_board)] = {
                    'array': final_board,
                    'steps': -1,
                    'moves': -1,
                    'final_mapping': -1
                }
            x += 1

    def save_patterns(self):
        print('{} patterns'.format(len(self.pattern_dictionary)))
        File.save_binary('pattern_dictionary.bin', self.pattern_dictionary)


if __name__ == '__main__':
    pd = PatternDatabase()
    pd.find_patterns()
    pd.save_patterns()


