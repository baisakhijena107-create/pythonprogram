class rectangle:
    def __init__(self,L,B):
        self.L=L
        self.B=B
    def show(self):
        print("Length=",self.L)
        print("Breath=",self.B)
    def area(self):
        return self.L*self.B
    def perimeter(self):
        print("perimeter=",2*(self.L+self.B))
r=rectangle(3,5)
r.show()
print("area of rectangle=",r.area())
print("perimeter of rectangle=",r.perimeter())