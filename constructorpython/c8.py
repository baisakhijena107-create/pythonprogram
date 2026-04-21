class Test:
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            print("No values")
        elif y is None:
            print("One value:", x)
        else:
            print("Two values:", x, y)

t1 = Test()
t2 = Test(5)
t3 = Test(5, 10)