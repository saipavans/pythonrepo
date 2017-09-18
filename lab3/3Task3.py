import math

constant_coefficient = ((2/9801)*(2**0.5))

def estimate_pi():
	k = 0
	sum = 0
	while True:
		term_to_add =  (((math.factorial(4*k)) * (1103 + (26390 * k))) / ((math.factorial(k)**4) * (396)**(4*k)))
		sum = sum + term_to_add
		k = k+1
		if term_to_add < (10**(-15)):
			break
	return (1/(sum*constant_coefficient))

print(estimate_pi())
