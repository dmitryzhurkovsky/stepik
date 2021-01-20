class multifilter:
    def judge_half(self, pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(self, pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(self, pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            pos, neg = 0, 0
            if self.i < len(self.iterable):
                for func in self.funcs:
                    if func(self.i) is True:
                        pos += 1
                    else:
                        neg += 1
                self.i += 1
                if self.judge(self, pos, neg) is True:
                    return self.iterable[self.i - 1]
            else:
                raise StopIteration


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]
print(a)

print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
