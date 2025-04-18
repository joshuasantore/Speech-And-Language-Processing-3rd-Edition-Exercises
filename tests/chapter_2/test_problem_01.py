import pytest
from problems.chapter_2.problem_01 import solution_1, solution_2, solution_3

'''
Write regular expressions for the following languages.
	1. the set of all alphabetic strings
    2. the set of all lower case alphabetic strings ending in a b
    3. the set of all strings from the alphabet a,b such that each a is immediately preceded by and immediately followed by a b
'''

'''@pytest.mark.parametrize("input_str,expected", [
    ("aBc", "aBc")
])

def test_solution_1(input_str, expected):
    assert solution_1(input_str) == expected



@pytest.mark.parametrize("input_str,expected", [
    ("abcd", "ab"),
    ("ab", "ab")
])

def test_solution_2(input_str, expected):
    assert solution_2(input_str) == expected
    

'''
@pytest.mark.parametrize("input_str,expected", [
    ("babab", "babab"),
    ("babb", "babb"),
    ("abb", "bb")
]) 
def test_solution_3(input_str, expected):
    assert solution_3(input_str) == expected
    


