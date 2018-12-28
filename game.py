import random
from dictionary_convertation import ij_count
guess_count = 0

def feedback(word, guess_count):
	sel_word_length = len(sel_word) - ij_count(str(sel_word)) - 1
	word_length = len(word) - ij_count(str(word))
	if sel_word_length != word_length:
		print("woord moet minstens 6 letters zijn")
		return guess_count

	if word[0] != sel_word[0]:
		print("begin letter moet hetzelfde zijn")
		return guess_count

	with open("nl_words_6.txt", "r") as check:
		if word + "\n" not in check:
			print("ongeldig woord")
			guess_count += 1
			print(guess_count)
			return guess_count
	
	if word + "\n" == sel_word:
		exit("goed gedaan!")

	# werkt nog niet voor rood en geel
	for index in range(len(word)):
		if word[index] == sel_word[index]:
			print(word[index] + ":" + "g")
		elif word[index] in sel_word[index:]:
			print(word[index] + ":" "r")
		else:
			print(word[index])
	print("--------")
	guess_count += 1
	print(guess_count)
	return guess_count

if __name__ == "__main__":
	with open("nl_words_6.txt", "r") as dictfile:
		lines = dictfile.readlines()
		sel_word = lines[random.randrange(len(lines))]
		print(sel_word)

	while (guess_count < 6):
		print(sel_word[0])
		beurt = input("")
		guess_count = feedback(beurt, guess_count)
		print(guess_count)
	
	print("goed geprobeerd")


