class Iterator():
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= 5:
            self.i += 1
            return 0
        else:
            raise StopIteration

x = Iterator()


print(x[2])