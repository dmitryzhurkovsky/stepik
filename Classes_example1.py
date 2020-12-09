class MoneyBox:
    def __init__(self, capcity):
        self.money = 0
        self.capcity = capcity

    def can_add(self, v):
        return self.money + v <= self.capcity

    def add(self, v):
        if self.can_add(v):
            self.money += v
