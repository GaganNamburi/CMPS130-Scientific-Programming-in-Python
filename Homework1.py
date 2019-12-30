#Returns true if value is a prime number
def isPrime(value):
	
	#Anything less than 2 is not prime
	if value < 2:
		return False

	#Check if anything greater than 1 is prime
	for i in range(2, value):
		if(value % i) == 0:
			return False
	return True

#Reverses value
def reverse(value):
	return int(str(value)[::-1])

#Ask user to enter positive number
value = 0
while value < 1:
	value = int(input("Please enter a positive number: "))
test = 2
i = 1

#Prints the emirps in rows of 5
while i <= value:
	if isPrime(test) == True:
		r = reverse(test)
		if isPrime(r) == True:
			if i % 5 == 0:
				print(test)
			else:
				print(test, end="\t")
			i += 1
	test += 1
