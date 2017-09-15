x = 10
a = 4
def square_root(a):
	global x
	epsilon = 0.0000001
	while True:
		print (x)
		y = ((x+(a/x))/2)
		if abs(y-x) < epsilon:
			break
		x = y
	return (x)

print("Square root of ", a, " is: ",square_root(a))
		
