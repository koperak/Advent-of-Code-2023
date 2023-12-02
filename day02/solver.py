import sys

from aoc import utils

measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    """returns: dictionary"""
    game_data = {}
    for game in raw_data.split("\n"):
        game_info = game.split(":")
        game_num = game_info[0].strip().split(" ")[1]
        game_sets = game_info[1].strip().split(";")

        game_data[game_num] = []

        for game_set_str in game_sets:
            game_set = game_set_str.split(",")
            bag = {}
            for bag_str in game_set:
                bag_info = bag_str.strip().split()
                bag_qty = int(bag_info[0])
                bag_color = bag_info[1]
                bag[bag_color] = bag_qty
            game_data[game_num].append(bag)

    return game_data


# PART 1
@measure_time
def solve1(data):
    game_sum = 0
    for game, game_sets in data.items():
        game_set_valid = []
        for game_set in game_sets:
            for bag_color, bag_qty in game_set.items():
                if (
                    (bag_color == "red" and bag_qty <= 12)
                    or (bag_color == "green" and bag_qty <= 13)
                    or (bag_color == "blue" and bag_qty <= 14)
                ):
                    game_set_valid.append(True)
                else:
                    game_set_valid.append(False)
        if all(game_set_valid):
            game_sum += int(game)
    return game_sum


# PART 2
@measure_time
def solve2(data):
    from math import prod
    game_sum = 0
    for game, game_sets in data.items():
        game_set_valid = {"red": [], "green": [], "blue": []}
        for game_set in game_sets:
            for bag_color, bag_qty in game_set.items():
                game_set_valid[bag_color].append(bag_qty)
        game_sum += prod([max(x) for x in game_set_valid.values()])
    return game_sum


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
