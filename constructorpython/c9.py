class Demo:
    def __del__(self):
        print("Object destroyed")

d = Demo()