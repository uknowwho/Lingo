import sys

def dictionarymaker(length, dictfile):
	with open("nl_words.txt", "r") as fileIn, open(dictfile, "w") as file_out:
		for line in fileIn:
			if len(line) == length + 1:
				if character_verification(line) and ij_verification(line):
					file_out.write(line)

			if len(line) == length:
				if character_verification(line) and not ij_verification(line):
					file_out.write(line)

def character_verification(line):
	banned_chars = ["-", "'", ".", " "]
	for index in range(len(line)):
		if line[index] in banned_chars or line[index].isupper():
			return False
	else:
		return True

def ij_verification(line):
	for index in range(len(line)):
		if line[index] == "i" and line[index + 1] == "j":
			return True
	else:
		return False


if __name__ == "__main__":
	# length is actually one higher
	dictionarymaker(7, "nl_words_6.txt")
	