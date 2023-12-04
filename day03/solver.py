import sys

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return [list(line) for line in raw_data.split("\n")]            


@measure_time
def iterate_matrix(start_x, start_y, end_x, end_y, max_point):
    result = []
    for i in range(start_y - 1, end_y + 2):
        for j in range(start_x - 1, end_x + 2):
            if 0 <= i <= max_point and 0 <= j <= max_point:
                if j < start_x or j > end_x or i < start_y or i > end_y:
                    result.append((j,i))

                    # Include diagonal points
                    if i != start_x and i != end_x and j != start_y and j != end_y:
                        diagonal_x = start_x + (i - start_x)
                        diagonal_y = start_y + (j - start_y)
                        print(f"Diagonal Point: ({diagonal_x}, {diagonal_y})")
    return result

# PART 1
@measure_time
def solve1(data):
    pass


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

