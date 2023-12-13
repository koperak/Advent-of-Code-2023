import sys
from functools import reduce

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return [list(map(int, output.split(" "))) for output in raw_data.split("\n")]


def calculate_difference(input):
    '''
    input - list of measures (int)
    returns - list of list of differences
    '''

    result_list = []

    difference_list = [b - a for (a,b) in list(zip(input, input[1::]))]

    result_list.append(difference_list)

    if set(difference_list) != {0}:
        result_list.extend(calculate_difference(difference_list))

    return result_list

# PART 1
@measure_time
def solve1(data):

    extrapolated_values_list = []
    difference = 0

    for data_line in data:
        extrapolated_values_list = [data_line[-1]] + [_[-1] for _ in calculate_difference(data_line)]
        difference = difference + reduce(lambda x, y: x + y, extrapolated_values_list)

    return difference


# PART 2
@measure_time
def solve2(data):

    extrapolated_values_list = []
    difference = 0

    for data_line in data:
        extrapolated_values_list = [data_line[0]] + [_[0] for _ in calculate_difference(data_line)]
        difference = difference + reduce(lambda x, y: y - x, reversed(extrapolated_values_list[:-1:]))

    return difference


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))

