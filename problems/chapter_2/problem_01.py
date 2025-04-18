import re
'''
Write regular expressions for the following languages.
	1. the set of all alphabetic strings
    2. the set of all lower case alphabetic strings ending in a b
    3. the set of all strings from the alphabet a,b such that each a is immediately preceded by and immediately followed by a b
'''

def solution_1(string):
	match = re.search("[a-zA-Z]+", string)
	if match:
		return match.group()
	return ""

def solution_2(string):
	match = re.search("[a-z]*b", string)
	if match:
		return match.group()
	return ""
	
def solution_3(string):
	match = re.search("b+(b?(ab)*)*", string)
	if match:
		return match.group()
	return ""
