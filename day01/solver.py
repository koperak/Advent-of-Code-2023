import sys
import re

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return raw_data.split("\n")


# PART 1
@measure_time
def solve1(data):
    liczby = []
    for line in data:
        _digits = [x for x in list(line) if str.isdecimal(x)]
        liczby.append(_digits[0:1][0] + _digits[-1:][0])

    return sum([int(x) for x in liczby])


# PART 2
def multi_replace(rules, _data: str) -> str:
    ret = _data
    for pattern, repl in rules:
        ret = re.sub(pattern, repl, ret)
    return ret


RULES = [
    (r"zero", r"z0o"),
    (r"one", r"o1e"),
    (r"two", r"t2o"),
    (r"three", r"t3e"),
    (r"four", r"f4r"),
    (r"five", r"f5e"),
    (r"six", r"s6x"),
    (r"seven", r"s7n"),
    (r"eight", r"e8t"),
    (r"nine", r"n9e"),
]

@measure_time
def solve2(data):
    newdata = [multi_replace(RULES, i) for i in data]
    return solve1(newdata)


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
