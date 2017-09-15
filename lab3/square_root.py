import math

x = 5

def square_root(a):
	global x
	epsilon = 0.0000001
	while True:
		#print (x)
		y = ((x+(a/x))/2)
		if abs(y-x) < epsilon:
			break
		x = y
	return (x)

def display_chi_square(a,b): 
	for i in range (a,b):
        	square_root_standard = float(math.sqrt(i))
        	square_root_custom = float(square_root(i))
        	difference = abs(square_root_standard - square_root_custom)
        	print (i , " " , square_root_standard , " " , square_root_custom , " ----" , difference)

		
