import re
'''
Implement an ELIZA-like program, using substitutions such as those described
on page 9. You might want to choose a different domain than a Rogerian psychologist, although keep in mind that you would need a domain in which your
program can legitimately engage in a lot of simple repetition.
'''

'''
My Program: Home Assistant

Given some instruction subsitutes, words and adds verb endings such that it is a confirmation that the task is being done.
'''

def solution(str):
	return re.sub(r"^(wash|add|delet|remov|creat|start)(e)?)\b(.*)", r"\1ing\3", str)
