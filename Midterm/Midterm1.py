x = int(input("Please enter a number between 2 and 5:	"))
while x < 2 or x > 5:
	x = int(input("Sorry, {} is not between 2 and 5, try again:	".format(x)))
print("Great!")
