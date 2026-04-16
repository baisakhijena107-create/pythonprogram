class employee:
	def __init__(self,a,n,sal):
		self.a=a
		self.nm=n
		self.salary=sal
	def show(self):
		print("my name=",self.nm)
		print("my age=",self.a)
		print("my salary=",self.salary)
s=employee(25,"Abhi",550000)
s.show()
s2=employee(21,"Khushi",60000)
s.show()
s=employee(22,"Tuhin",55000)
s.show()
s=employee(22,"Ameer",10000)
s.show()
s=employee(20,"Inshan",40000)
s.show()