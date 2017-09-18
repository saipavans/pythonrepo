input_string = input("enter input")
len = len(input_string)
if len >= 3:
	trial = input_string[len-3 : len]
	if trial == "ing":
		print(input_string + "ly")
	else:
		print(input_string + "ing")

else:
	print(input_string)
