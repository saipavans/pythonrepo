result = 0

def nested_sum(nested_number_list):
	global result
	for element in nested_number_list:
		if isinstance(element, list):
			nested_sum(element)
		else:
			result+= element
	return(result)

print(nested_sum([1,2,3,[1,2,3]])) 	
			
