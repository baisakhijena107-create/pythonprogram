class student:
	def __init__(self):
		self.__marks=90
	def __show(self):
		print("Private Method")
	def access_private(self):
		print(self.__marks)
		self.__show()
s=student()
s.access_private()