import pytest
from solver import parse, solve1, solve2

TESTDATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)

TESTDATA2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

@pytest.fixture
def parsed_data2():
    return parse(TESTDATA2)


def test_parse():
    data = parse(TESTDATA)
    # asserts go here


# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 142


# PART 2
def test_solve2(parsed_data2):
    solution = solve2(parsed_data2)
    assert solution == 281
