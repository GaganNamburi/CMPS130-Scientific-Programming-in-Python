class A:
	def x(self):
		print('X')

class B(A):
	def y(self):
		print('Y')

class C(A):
	def x(self):
		print('x')

	def z(self):
		print('Z')

class D(B):
	def z(self):
		print("z")

test = D()
