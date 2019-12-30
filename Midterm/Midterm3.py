x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))
z = int(input("Please enter a number: "))

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
	print("A")
elif x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
	print("B")
elif x == y and x == z and y == z:
	print("C")
