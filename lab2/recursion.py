count = 0

def do_n(fun, n):
	global count
	count+=1
	if count<n:
		do_n(fun, n)
	display()

def display():
	print ("displaying ..")

do_n(display,10)
