class student:
	def __init__(self, marks):
		self.marks=marks
	def __gt__(self,other):
		return self.marks > other.marks

s1=student(80)
s2=student(60)

print(s1>s2)