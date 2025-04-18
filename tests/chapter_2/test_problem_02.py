import pytest
from problems.chapter_2.problem_02 import solution_1, solution_2, solution_3, solution_4


'''
Write regular expressions for the following languages.
	1. the set of all strings with two consecutive repeated words (e.g., “Humbert Humbert” and “the the” but not “the bug” or “the big bug”);
	2. all strings that start at the beginning of the line with an integer and that end at the end of the line with a word;
	3. all strings that have both the word grotto and the word raven in them (but not, e.g., words like grottos that merely contain the word grotto);
	4. write a pattern that places the first word of an English sentence in a register. Deal with punctuation.
'''

@pytest.mark.parametrize("input_str,expected", [
    ("humbert humbert", "humbert humbert"),
    ("oh", ""),
    ("word word not word", "word word")
    
])

def test_solution_1(input_str, expected):
    assert solution_1(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("1 number", "1 number"),
    ("12 is at the start and 1 is at the end", "12 is at the start and 1 is at the end"),
    ("just words", ""),
    ("2", "") 
])

def test_solution_2(input_str, expected):
    assert solution_2(input_str) == expected


@pytest.mark.parametrize("input_str,expected", [
    ("there is a raven in the grotto", "there is a raven in the grotto"),
    ("there are usually ravens in grottos", ""),
    ("just words", ""),
    ("2", "")
    
])

def test_solution_3(input_str, expected):
    assert solution_3(input_str) == expected



@pytest.mark.parametrize("input_str,expected", [
    ("Hello...", "Hello"),
    ("just some words", "just"),
    ("2", "")
    
])

def test_solution_4(input_str, expected):
    assert solution_4(input_str) == expected
