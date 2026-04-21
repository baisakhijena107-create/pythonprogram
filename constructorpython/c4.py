class Test:
    def __init__(self, x, y):   # parameterized constructor
        self.x = x
        self.y = y

t = Test(10, 20)
print(t.x, t.y)