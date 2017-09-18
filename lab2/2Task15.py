def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

######## task 15 - 1 ##########
word1 = "ab"
word2 = "a"
word3 = ""
print("testing middle with two letters ", middle(word1))
print("testing middle with one letter", middle(word2))
print("testing middle with empty string", middle(word3))


######## task 15-2 #############
def is_palindrome(word):
	result = True
	if len(word) > 2:
		if first(word) ==  last(word):
			is_palindrome(middle(word))
		else:
			result = False
	return(result)

print("checking the word redivider for palindrome", is_palindrome("redivider"))
print("checking the word redividend for palindrome", is_palindrome("redividend"))	
 
