words_total = 0
words_without_forbidden_letters = 0
forbidden_letters = ""
words_file_path = "../resources/words.txt"

def has_no_forbidden_letters(word, forbidden_letters):
	result = True
	for letter in forbidden_letters:
		if letter in word:
			result = False
			break
	return result

fin = open(words_file_path)
forbidden_letters = input("Enter forbidden string: ")


for line in fin:
	word = line.strip()
	words_total += 1
	if has_no_forbidden_letters(word, forbidden_letters):
		print(word)
		words_without_forbidden_letters += 1

print("number of words without forbidden letters: ", words_without_forbidden_letters)
print("percentage of words without forbidden letters : ",((words_without_forbidden_letters/words_total)*100))
