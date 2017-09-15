input_string = "saipavan"

def print_in_reverse(st):
	st_len = len(st)
	for i in range(st_len):
		print(st[st_len-i-1])
			

print("Priting the string ", input_string, " in reverse ..")
print_in_reverse(input_string)
