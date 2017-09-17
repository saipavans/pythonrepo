def right_justify(phrase):
	space = ' '
	stringLength = len(phrase)
	indent = 70 - stringLength 
	output = (space * indent) + phrase
	print(output)

right_justify("saipavan")

