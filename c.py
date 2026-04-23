class person :
	def __init__(self,name):
		self.name = name 
		print("person constructor called")
class student(person):
	def __init__(self,name):
		super().__init__(name)
		print("student constructor called")
s=student("Abhishek")