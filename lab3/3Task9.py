words_file_path = "../resources/words.txt"
fin = open(words_file_path)
words_exceeding_twenty_characters = 0
character_threshold = 20

for line in fin:
	word = line.strip()
	if len(word) > character_threshold:
		words_exceeding_twenty_characters = words_exceeding_twenty_characters + 1
		print(word)

print(words_exceeding_twenty_characters)
