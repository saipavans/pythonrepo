x = 10
a = 4
def square_root(a):
	global x
	while True:
		print (x)
		y = ((x+(a/x))/2)
		if y == x:
			break
		x = y
	return (x)

print("Square root of ", a, " is: ",square_root(a))
		
