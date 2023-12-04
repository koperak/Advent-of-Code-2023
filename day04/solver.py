import sys

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return raw_data.split("\n")


# PART 1
@measure_time
def solve1(data):
    return sum(map(lambda x: 2 ** (x -1) if x >0 else 0, [len(set(winning.strip().split()) & set(have.strip().split())) for winning, have in [card[7:].split("|") for card in data]]))


# PART 2
@measure_time
def solve2(data):
    pass


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))

