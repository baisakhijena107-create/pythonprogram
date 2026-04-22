class A:
	def show(self):
		print("Parent A")
class B(A):
	pass
class C(A):
	pass 
b=B()
c=C()
b.show()
b.show()