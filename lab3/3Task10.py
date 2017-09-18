words_total = 0
words_without_e = 0
words_file_path = "../resources/words.txt"

def has_no_e(word):
	result = True
	check_char = 'e'
	if check_char in word:
		result = False
	return result

fin = open(words_file_path)

for line in fin:
	word = line.strip()
	words_total += 1
	if has_no_e(word):
		print(word)
		words_without_e += 1

print((words_without_e/words_total)*100)
