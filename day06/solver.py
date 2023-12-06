import sys
import re

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return [{line[0]:re.sub(r"\s+", " ", line[1].strip()).split(" ")} for i, line in enumerate([time_line.split(":") for time_line in raw_data.split("\n")])]


# PART 1
@measure_time
def solve1(data):
    import math
    v = 1
    winning_option = []
    winning = []
    for (t, s) in  list(zip(data[0]['Time'], data[1]['Distance'])):
        t = int(t)
        s = int(s)
        winning_option = []
        for option in range(t + 1):
            speed = option # speed depends how long button hold 
            time = t - option # time the boat will travel
            distance = time * speed
            if distance  > s:
                winning_option.append(option)
        winning.append(winning_option)
    return math.prod([len(_) for _ in winning])


# PART 2
@measure_time
def solve2(data):
    import math
    v = 1
    winning_option = []
    winning = []
    # for (t, s) in  list(zip("".join(data[0]['Time']), "".join(data[1]['Distance']))):
    t = int("".join(data[0]['Time']))
    s = int("".join(data[1]['Distance']))
    winning_option = []
    for option in range(t + 1):
        speed = option # speed depends how long button hold 
        time = t - option # time the boat will travel
        distance = time * speed
        if distance  > s:
            winning_option.append(option)
    winning.append(winning_option)
    return (math.prod([len(_) for _ in winning]))


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))

