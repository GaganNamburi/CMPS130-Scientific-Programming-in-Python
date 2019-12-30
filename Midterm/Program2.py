terms = 41
while terms > 40:
	terms = int(input("Please enter a number: "))

global space
space = input("What character would you like to fill the spaces with: ")
if space == "":
	space = "#"

global char
char = input("What character would you like to fill the diamond with: ")
if char == "":
	char = "+"

def print_chars(character, times):
	p =  character*times
	print(p, end="")

def print_line(spaces, stars):
	global space
	global char
	print_chars(space, spaces)
	print_chars(char, stars)
	print(space)

#First half
spaces = terms - 1
stars = 1
for i in range(terms):
	print_line(spaces, stars)
	spaces -= 1
	stars += 2

#Second half
spaces = 1
stars -= 4
for i in range(terms - 1):
	print_line(spaces, stars)
	spaces += 1
	stars -= 2
