'''Write a program to compute unsmoothed unigrams and bigrams.'''

import re
import random

def tokenizer(text:str):
	# Prepare text to be segmented
	text = re.sub(r"[—;:'’,/\\\*@#$%\^&\(\)\<\>\{\}]", "", text) # remove not sentence ending punctuation
	text = re.sub(r"(  |\s)", " ", text) # Remove double spaces and tabs etc
	
	# normalize words
	text = text.lower() # remove capitalization

	# segment
	text = re.sub(r"[.?!]", " </s>", text) # replace sentence ending punctuation with proper marker

	
	# segment text into tokens
	return text.split(" ")


def unigram(text: str, sentence: bool = True):
	
	# tokenize
	tokens = tokenizer(text)

	# parse vocabulary
	vocab = []
	seen = set()
	for token in tokens:
		if token not in seen:
			vocab.append(token)
			seen.add(token)

	# generate unigram probabilities
	unigram = {}
	for token in vocab:
		unigram[token]= tokens.count(token)/len(tokens) # really should wrap in math.log()

	# display ngrams sorted by length
	sortedunigrams = sorted(unigram.items(), key=lambda item: item[1])
	sortedunigrams.reverse()
	print(sortedunigrams)

	# generate a sentence
	if sentence:
		sent = []
		# generate a probability line for tokens
		distribution = build_cum_dist(sortedunigrams)

		unigram = pick_unigram(distribution)

		while unigram != "</s>":
			sent.append(unigram)
			unigram = pick_unigram(distribution)
		
		print(" ".join(sent))




def build_cum_dist(sortedunigrams: list[tuple]):
	start = 0
	end = 0
	dist = {}
	for i in range(len(sortedunigrams)):
		if i == len(sortedunigrams) - 1:
			end = 1
		else:
			end += sortedunigrams[i][1]
		dist[(start, end)] = sortedunigrams[i][0]
		start = end
	
	return dist

def pick_unigram(distribution:dict):

	generated = random.random()

	for interval in list(distribution.keys()):
		if interval[0] <= generated < interval[1]:
			return (distribution[interval])


unigram("Before the courts, both in law and custom, they stand on a different and peculiar basis. Taxation without representation is the rule of their political life.", sentence = True)
