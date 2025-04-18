import re
'''
Write regular expressions for the following languages.
	1. the set of all strings with two consecutive repeated words (e.g., “Humbert Humbert” and “the the” but not “the bug” or “the big bug”);
	2. all strings that start at the beginning of the line with an integer and that end at the end of the line with a word;
	3. all strings that have both the word grotto and the word raven in them (but not, e.g., words like grottos that merely contain the word grotto);
	4. write a pattern that places the first word of an English sentence in a register. Deal with punctuation.
'''

def solution_1(string):
	match = re.search(r"([a-zA-Z]+) \1", string)
	if match:
		return match.group()
	return ""

def solution_2(string):
	match = re.search(r"^[0-9]+.* [a-zA-Z]+$", string)
	if match:
		return match.group()
	return ""
	
def solution_3(string):
	match = re.search(r"^(?=.*\bgrotto\b)(?=.*\braven\b).*$", string)
	if match:
		return match.group()
	return ""

def solution_4(string):
	match = re.search(r'[\W]*([a-zA-Z]+)(a-zA-Z )*[\W]*', string)
	if match:
		return match.group(1)
	return ""
