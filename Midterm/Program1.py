def LCM(num1, num2):
	#Same number means LCM already found
	if num1 == num2:
		return num1

	#Bigger number
	if num1 > num2:
		multi = num1
	else:
		multi = num2

	#Bigger number iterates until there is a number that has no remainder for both
	while(True):
		if multi % num1 == 0 and multi % num2 == 0:
			return multi
			break
		multi += 1

x = 0
while x < 1:
	x = int(input("Please enter a positive integer: "))
y = 0
while y < 1:
	y = int(input("Please enter a positive integer: "))

#Output statement
print("LCM is", LCM(x, y))
