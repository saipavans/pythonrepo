words_total = 0
words_with_required_letters = 0
required_letters = ""
words_file_path = "../resources/words.txt"

def uses_all(word, required_letters):
	result = True
	for letter in required_letters:
		if letter in word:
			continue
		else:
			result = False
			break
			
	return result

fin = open(words_file_path)
required_letters = input("Enter required letters: ")


for line in fin:
	word = line.strip()
	words_total += 1
	if uses_all(word, required_letters):
		print(word)
		words_with_required_letters += 1

print("number of words with required letters: ", words_with_required_letters,words_total)
print("percentage of words with required letters : ",((words_with_required_letters/words_total)*100))
print(uses_all("abca","q"))
