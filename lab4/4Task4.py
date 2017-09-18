multiple = 7
is_multiple = lambda n : n%multiple == 0
input_list = range(0,101)
result = list(filter(is_multiple, input_list))
print(result)
