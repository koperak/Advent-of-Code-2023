import pytest
from solver import parse, solve1, solve2

TESTDATA = """Time:      7  15   30
Distance:  9  40  200"""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


def test_parse():
    data = parse(TESTDATA)

# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 288


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    assert solution == 71503
