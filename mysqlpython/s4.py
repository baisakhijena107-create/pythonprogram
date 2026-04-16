class student:
	def __init__(self,r,n,m):
		self.r=r
		self.nm=n
		self.mark=m
	def show(self):
		print("my name=",self.nm)
		print("my rollno=",self.r)
		print("my mark=",self.mark)
s=student(1,"ram",90.50)
s.show()