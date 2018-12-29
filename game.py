import random
from dictionary_convertation import ij_count

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
			return guess_count
	
	if word + "\n" == sel_word:
		exit("goed gedaan!")

	# TODO
	# werkt nog niet voor rood en geel
	# werkt nog niet voor ij
	# oplossing: stop feedback in list
	# tel hoe vaak letter voorkomt
	# hou volgorde aan: geel, rood, blanco
	# alleen feedback geven als occurrence niet 0 is
	# functie die list showt, zoals bij echt lingo
	# met ij als 1 letter

	word_dict = {}
	for index in range(len(word)):
		if word[index] == "i" and word[index + 1] == "j":
			if "ij" not in word_dict:
				word_dict["ij"] = 1
			else:
				word_dict["ij"] += 1
		elif word[index] == "j" and word[index - 1] == "i":
			pass
		elif word[index] not in word_dict:
			word_dict[word[index]] = 1
		else:
			word_dict[word[index]] += 1

	feedback_word = {}

	for index in range(len(word)):
		if word[index] == "i" and word[index + 1] == "j":
			if sel_word[index] == "i" and sel_word[index + 1] == "j":
				feedback_word["ij"] = ":r" 
		elif word[index] == "j" and word[index - 1] == "i":
			pass
		elif word[index] == sel_word[index]:
			feedback_word[word[index]] = ":r"
			word_dict[word[index]] -= 1

	print(word_dict)
	print(feedback_word)
	guess_count += 1
	return guess_count

	# for index in range(len(word)):
	# 	if word[index] == sel_word[index]:
	# 		print(word[index] + ":" + "g")
	# 	elif word[index] in sel_word[index:]:
	# 		print(word[index] + ":" "r")
	# 	else:
	# 		print(word[index])
	# print("--------")
	# guess_count += 1
	# return guess_count

if __name__ == "__main__":
	guess_count = 0
	with open("nl_words_6.txt", "r") as dictfile:
		lines = dictfile.readlines()
		#sel_word = lines[random.randrange(len(lines))]
		sel_word = "zijbeuk\n"
		print(sel_word)

	while (guess_count < 6):
		print(sel_word[0])
		beurt = input("")
		guess_count = feedback(beurt, guess_count)
	
	print("goed geprobeerd")
