def dictionary_option(length, dictfile):
	with open("nl_words.txt", "r") as fileIn, open ("nl_words_lengths.txt", "w") as fileOut:
		for line in fileIn:
			# filter all words that are not egligable
			if character_verification(line):
				# calculate length of every word and add it as word,length
				line_length = len(line) - ij_count(str(line)) - 1
				line = line.splitlines()[0]
				fileOut.write(line + "," + str(line_length) + "\n")

	with open("nl_words_lengths.txt", "r") as fileInnit, open(dictfile, "w") as fileOutit:
		for line in fileInnit:
			if line.split(",")[1] == str(length) + "\n":
				fileOutit.write(line.split(",")[0]+ "\n")
	
def character_verification(line):
	banned_chars = ["-", "'", ".", " "]
	for index in range(len(line)):
		if line[index] in banned_chars or line[index].isupper():
			return False
	else:
		return True

# calculates amount of ij's in a given word
def ij_count(word):
	ij_counter = 0
	for index in range(len(word)):
		if word[index] == "i" and word[index + 1] == "j":
			ij_counter += 1
	return int(ij_counter)


if __name__ == "__main__":
	# length is one higher
	dictionary_option(6, "nl_words_test.txt")
