class Test:
    def __init__(self, x=0, y=0):   # default parameter constructor
        self.x = x
        self.y = y

t1 = Test()          # uses default values
t2 = Test(5, 10)     # uses given values

print(t1.x, t1.y)
print(t2.x, t2.y)