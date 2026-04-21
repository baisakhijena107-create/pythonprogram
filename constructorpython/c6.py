class Test:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

t1 = Test()        # no argument
t2 = Test(10)      # one argument
t3 = Test(10, 20)  # two arguments

print(t1.x, t1.y)
print(t2.x, t2.y)
print(t3.x, t3.y)