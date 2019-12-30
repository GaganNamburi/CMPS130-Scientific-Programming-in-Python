x = 5
y = 9
global z
def foo(x):
	x = 8
	y = 10
	def fizz():
		global z
		z = 10
		return z + y
	z = x + y
	#What is x, y, z
	return z
def bar(z):
	y = 20
	#X, y, z
	return z + y
z = 16
w = (foo(x)+bar(x))
#X, y, z
