def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def check_nested_list(input_list):
	for element in input_list:
		if isinstance(element,list):
			return True
	return False

def capitalize_nested(nested_string_list):
	res = []
	if isinstance(nested_string_list,list):
		if check_nested_list(nested_string_list):
			for element in nested_string_list:
				if isinstance(element,list):
					res = res + (capitalize_nested(element))
				else:
					res.append(element.capitalize())
		else: ## LIST, BUT NOT NESTED
			res = res + (capitalize_all(nested_string_list))
	return res

input = ["sai","pavan",["dalhousie","inwk"]]
print(capitalize_nested(input))
		
			
