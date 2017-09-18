import functools

s = lambda x,y : x+y
input_list = []


for num in range(100,501):
	if num%2 == 0:
		input_list.append(num) 
print(input_list)
result = functools.reduce(s,input_list)
print(result)

