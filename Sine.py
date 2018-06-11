import math

def my_sine(p):
	sum = 0
	for n in range(85):
		sum += ((-1)**(n))*((p)**(2*n+1))/(math.factorial(2*n+1))
	return sum

angle = math.pi/2
print(my_sine(angle))

angle = math.pi
print(my_sine(angle))

angle = 3*math.pi/2
print(my_sine(angle))

angle = 2*math.pi
print(my_sine(angle))
