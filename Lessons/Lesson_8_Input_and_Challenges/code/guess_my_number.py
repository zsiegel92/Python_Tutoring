import random

print("Enter a lower bound for random numbers")
minimum = int(input())
maximum = minimum
while maximum <= minimum:
	print("Enter an upper bound for random numbers")
	maximum = int(input())
secret = random.randint(minimum,maximum)
x = secret + 1

while x != secret:
	print("Guess a number between {} and {}".format(minimum,maximum))
	x = int(input())
	if x < secret:
		print("Too low!")
	elif x > secret:
		print("Too high!")
print("You got it!")
