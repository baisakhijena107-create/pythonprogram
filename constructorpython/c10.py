class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, "w")
        print("File opened")

    def __del__(self):
        self.file.close()
        print("File closed")

f = FileHandler("test.txt")