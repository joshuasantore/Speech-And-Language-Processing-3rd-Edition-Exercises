import pytest
from problems.chapter_2.problem_03 import solution
'''
Implement an ELIZA-like program, using substitutions such as those described
on page 9. You might want to choose a different domain than a Rogerian psychologist, although keep in mind that you would need a domain in which your
program can legitimately engage in a lot of simple repetition.
'''


@pytest.mark.parametrize("input_str,expected", [
    ("wash the clothes", "washing the clothes"),
    ("add to calendar", "adding to calendar"),
    ("delete the blog post", "deleting the blog post"),  
])

def test_solution(input_str, expected):
	assert solution(input_str) == expected
