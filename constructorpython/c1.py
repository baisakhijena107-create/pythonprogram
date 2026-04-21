class Student:
    def __init__(self, r, n, m):   # constructor
        self.roll = r
        self.name = n
        self.mark = m

    def display(self):
        print("Roll:", self.roll)
        print("Name:", self.name)
        print("Mark:", self.mark)

# object creation
s1 = Student(1, "Ram", 90)

s1.display()