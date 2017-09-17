def do_twice(f,v):
	f(v)
	f(v)

def print_twice(phrase):
	print(phrase)

do_twice(print_twice, 'spam')


##  part 5 ##
print("output of 5th part")

def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
do_four(print_twice, 'spam')
