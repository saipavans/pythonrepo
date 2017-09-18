def is_triangle(a,b,c):
	bool1 = a>(b+c)
	bool2 = b>(a+c)	
	bool3 = c>(a+b)
	if (bool1 or bool2 or bool3):
		print("NO")
	else:
		print("YES")


a = int (input("enter a "))
b = int (input("enter b "))
c = int (input("enter c "))

is_triangle(a,b,c)
	
