import pytest
from solver import parse, solve1, solve2, mapping_categories

TESTDATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

@pytest.fixture
def parsed_data():
    return parse(TESTDATA)


def test_parse():
    data = parse(TESTDATA)
    # asserts go here


def test_mapping():
    data = parse(TESTDATA)
    assert 13 == mapping_categories(13, data[1][1])
    assert 14 == mapping_categories(14, data[1][1])
    assert 57 == mapping_categories(55, data[1][1])
    
    assert 81 == mapping_categories(79, data[1][1])
    assert 81 == mapping_categories(81, data[2][1])
    assert 81 == mapping_categories(81, data[3][1])
    assert 74 == mapping_categories(81, data[4][1])
    assert 78 == mapping_categories(74, data[5][1])
    assert 78 == mapping_categories(78, data[6][1])
    assert 82 == mapping_categories(78, data[7][1])

    assert 14 == mapping_categories(14, data[1][1])
    assert 53 == mapping_categories(14, data[2][1])
    assert 49 == mapping_categories(53, data[3][1])
    assert 42 == mapping_categories(49, data[4][1])
    assert 42 == mapping_categories(42, data[5][1])
    assert 43 == mapping_categories(42, data[6][1])
    assert 43 == mapping_categories(43, data[7][1])



# PART 1
def test_solve1(parsed_data):
    solution = solve1(parsed_data)
    assert solution == 35


# PART 2
def test_solve2(parsed_data):
    solution = solve2(parsed_data)
    # asserts go here
