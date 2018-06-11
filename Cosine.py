import math

def my_Cosine(p):
	sum = 0
	for n in range(86):
		sum += ((-1)**(n))*((p)**(2*n))/(math.factorial(2*n))
	return sum

angle = math.pi/2
print(my_Cosine(angle))

angle = math.pi
print(my_Cosine(angle))

angle = 3*math.pi/2
print(my_Cosine(angle))

angle = 2*math.pi
print(my_Cosine(angle))

