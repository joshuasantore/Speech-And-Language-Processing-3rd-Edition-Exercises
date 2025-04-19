import pytest
from problems.chapter_2.problem_06 import minimum_edit_distance1, minimum_edit_distance2
'''
Implement a minimum edit distance algorithm and use your hand-computed
results to check your code.
'''


@pytest.mark.parametrize("input1,input2,expected", [
    ("big", "dig", 1),
	("drive", "divers", 3),
	("drive", "brief", 3)

])

def test_minimum_edit_distance_1(input1, input2, expected):
	assert minimum_edit_distance1(input1, input2) == expected


@pytest.mark.parametrize("input1,input2,expected", [
    ("big", "dig", 2),
	("drive", "divers", 3),
	("drive", "brief", 4)

])

def test_minimum_edit_distance_2(input1, input2, expected):
	assert minimum_edit_distance2(input1, input2) == expected
