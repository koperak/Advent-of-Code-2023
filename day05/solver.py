import sys

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    result = []
    for instruction in [line.split(":") for line in raw_data.split("\n\n")]:
        if instruction[0] == "seeds":
            instruction[1] = list(map(int, instruction[1].strip().split(" ")))
        else:
            instruction[1] = [
                list(map(int, _elem.split(" ")))
                for _elem in instruction[1].split("\n")
                if _elem != ""
            ]
        result.append(instruction)
    return result


def mapping_categories(source_item: int, mapping: list) -> int:
    for _map in mapping:
        destination_start, source_start, range_len = _map[0], _map[1], _map[2]
        if source_item < source_start:
            continue
        elif source_start <= source_item <= source_start + range_len:
            source_item = source_item + destination_start - source_start
            break
    return source_item


81 == mapping_categories(77, [[45, 77, 23], [81, 45, 19], [68, 64, 13]])
42 == mapping_categories(53, [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]])


@measure_time
def solver(soil, data):
    result = []
    i = soil
    for j in data[1:]:
        i = mapping_categories(i, j[1])
    return i


# PART 1
@measure_time
def solve1(data):
    result = []
    for i in data[0][1]:
        result.append(solver(i, data))
q    return min(result)


# PART 2
@measure_time
def solve2(data):
    minx = zamiana = _oszk = 0
    result = []
    for zi in range(0, len(data[0][1]), 2):
        iterek = 0
        startx = data[0][1][zi]
        endx = data[0][1][zi + 1] + data[0][1][zi]
        while startx < endx:
            #seed_list.append(startx)
            _oszk = solver(startx, data)
            startx = startx + 1
            if minx == 0:
                minx = startx
            if minx >= _oszk:
                minx = _oszk
    return minx


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
