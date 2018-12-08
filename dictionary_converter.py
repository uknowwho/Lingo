import sys

def dictionarymaker(length, dictfile):
	with open("nl_words.txt", "r") as nl_dict:
		sys.stdout=open(dictfile,"w")
		for word in nl_dict:
			# adds the correct words with "ij" in them
			if len(word) == length + 1 and word[0].islower():
				for i in range(len(word) - 1):
					if word[i] == "'" or word[i] == "." or word[i] == "-" or word[i] == " ":
						break
					if word[i] == 'i' and word[i + 1] == 'j':
						print(word, end="")
			# adds the correct words with the correct length
			if len(word) == length and word[0].islower():
				for i in range(len(word) - 1):
					if word[i] == 'i' and word[i + 1] == 'j':
						break
					if word[i] == "'" or word[i] == "." or word[i] == "-" or word[i] == " ":
						break
				# if we've reached here we're safe to write the word
				else:
					print(word, end="") 
		sys.stdout.close()
# add code that deletes jij-bak

if __name__ == "__main__":
	# length is actually one higher
	dictionarymaker(7, "nl_words_6.txt")
