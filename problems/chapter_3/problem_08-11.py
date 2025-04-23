'''Write a program to compute unsmoothed unigrams and bigrams.'''

import re
import random

def tokenizer(text:str, n:int = 1):
	# Prepare text to be segmented
	text = re.sub(r"[—;:'’,/\\\*@#$%\^&\(\)\<\>\{\}]", "", text) # remove not sentence ending punctuation
	text = re.sub(r"(  |\s)", " ", text) # Remove double spaces and tabs etc
	
	# normalize words
	text = text.lower() # remove capitalization

	# segment
	if n!=1:
		text = re.sub(r"^","<s> "*(n-1), text) # add sentence beginning bracket to beginning of text
		text = re.sub(r"[.?!]", (" </s>" * (n-1)) + (" <s>"* (n-1)), text) # replace sentence ending punctuation with proper marker and mark the next sentence beginning
		text = text[:(-4*(n-1))] # remove final sentence beginning because there are no more
	
	text = re.sub(r"[.?!]", " </s>", text) # replace sentence ending punctuation with proper marker

	
	# segment text into tokens
	return text.split(" ")


def n_gram(text: str, n:int = 1, sentence: bool = True):
	
	# tokenize
	tokens = tokenizer(text, n=n)
	print(f"Tokens \n{tokens}\n")

	# parse vocabulary
	
	vocab = []
	seen = set()
	for token in tokens:
		if token not in seen:
			vocab.append(token)
			seen.add(token)

	# generate ngram probabilities
	ngrams = recursive_n_grams(n,vocab, tokens, [])
	
	
	# sort ngrams by probability
	sorted_ngrams = sorted(ngrams.items(), key=lambda item: item[1])
	sorted_ngrams.reverse()
	
	
	# print the nonzero grams
	print(f"{n}-gram Probabilities")
	i = 0
	while i < len(sorted_ngrams) and sorted_ngrams[i][1] > 0:
		print(sorted_ngrams[i])
		i+=1

	# generate a sentence
	if sentence:
		sent = []
		for i in range(n - 1):
			sent.append("<s>")
		
		
		choice = pick_ngram(sent, sorted_ngrams, n)
		while choice != "</s>":
			sent.append(choice)
			choice = pick_ngram(sent, sorted_ngrams, n)
			i+=1
		
		print("Sentence:")
		print(" ".join(sent[2:]))


def recursive_n_grams(n, vocab: list,tokens: list, tokenList: list):
	n_grams = {}
	if n != len(tokenList):
		for token in vocab: 
			n_grams.update(recursive_n_grams(n, vocab, tokens, tokenList+[token]))
		return n_grams
	else:
		if n == 1:
			history_count == len(tokens)
		else:
			history_count = " ".join(tokens).count(" ".join(tokenList[:-1]))
		if history_count > 0:
			ngram_count = " ".join(tokens).count(" ".join(tokenList))
			return {tuple(tokenList) : ngram_count/history_count}
		return {}
		

def build_cum_dist(sorted_ngrams: list[tuple], history=None):
	start = 0
	end = 0
	dist = {}
	if history is not None:
		for i in range(len(sorted_ngrams)):
			
			if sorted_ngrams[i][0][:-1] == tuple(history) and sorted_ngrams[i][1] != 0:
				end += sorted_ngrams[i][1]
				dist[(start, end)] = sorted_ngrams[i][0]
				start = end

	else:
		for i in range(len(sorted_ngrams)):
			if i == len(sorted_ngrams) - 1 :
				end = 1
			else:
				end += sorted_ngrams[i][1]
			dist[(start, end)] = sorted_ngrams[i][0]
			start = end
	
	return dist


def pick_ngram(sentence: list[str], sorted_ngrams:list[tuple], n:int = 1):
	# generate a distribution for ngrams according to the previous n-1 gram

	distribution = {}
	if n ==1:
		distribution = build_cum_dist(sorted_ngrams)
	else:
		distribution = build_cum_dist(sorted_ngrams, history=sentence[-(n-1):])

	generated = random.random()

	for interval in list(distribution.keys()):
		if interval[0] <= generated < interval[1]:
			return distribution[interval][-1]


n_gram("Sam I am. I am Sam. Sam I am. I do not like green eggs and ham", 
	   n=2, 
	   sentence = True
)
