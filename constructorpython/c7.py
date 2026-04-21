class Test:
    def __init__(self, *args):
        if len(args) == 0:
            print("No argument")
        elif len(args) == 1:
            print("One argument:", args[0])
        elif len(args) == 2:
            print("Two arguments:", args[0], args[1])

t1 = Test()
t2 = Test(10)
t3 = Test(10, 20)