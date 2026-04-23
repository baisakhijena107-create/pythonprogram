class employee:
	def salary (self):
		print("base salary")
class manager(employee):
	def salary(self):
		print("manager salary is higher")

m = manager()
m.salary()