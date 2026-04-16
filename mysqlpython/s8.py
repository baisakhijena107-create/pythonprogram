class square:
    def __init__(self,s):
        self.s=s
    def show(self):
        print("side=",self.s)
    def area(self):
        return self.s^2
    def perimeter(self):
        print("perimeter=",4*self.s)
r=square(4)
r.show()
print("area of square=",r.area())
print("perimeter of square=",r.perimeter())