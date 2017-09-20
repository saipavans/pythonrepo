
def find_cumilative_sum(input_list):
	res = []
	for i in range(len(input_list)):
		if len(res)!= 0:
			res.append(input_list[i] + res[i-1])
		else:
			res.append(input_list[i])
	return res

input_list = [1,2,3,4,5,6]
print(find_cumilative_sum(input_list))
			
