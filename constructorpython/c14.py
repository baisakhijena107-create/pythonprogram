class Math:
    @staticmethod
    def perimeter(l, b):
        return 2*(l + b)
    def area(l,b):    
        return l*b
print(Math.perimeter(10, 20))
print(Math.area(10,20))