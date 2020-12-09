class ExtendedStack(list):
    def sum(self):
        self.append(int(self.pop() + self.pop()))

    def sub(self):
        self.append(int(self.pop() - self.pop()))

    def mul(self):
        self.append(int(self.pop() * self.pop()))

    def div(self):
        self.append(int(self.pop() // self.pop()))


