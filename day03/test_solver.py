import pytest
from solver import parse, solve1, solve2, iterate_matrix

TESTDATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


def test_parse():
    data = parse(TESTDATA)
    assert data == [['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
                    ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
                    ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
                    ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
                    ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
                    ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']]


def test_iterate_matrix():
    assert iterate_matrix(0,0,0,2,9) == [(1,0), (1,1), (1,2), (0,3), (1,3)]
    assert iterate_matrix(9,5,9,8,9) == [(8,4), (9,4) ,(8,5), (8,6), (8,7), (8,8), (8,9), (9,9)]


# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 4361


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    # asserts go here
