import unittest


class InputData(object):
    def __init__(self):
        self.x1 = 1
        self.y1 = 5

        self.x2 = 3
        self.y2 = -7

        self.x3 = -3
        self.y3 = -10

        self.x4 = 0
        self.y4 = 5

        self.x5 = 4
        self.y5 = 0


class TestMathematicalOperation(unittest.TestCase, InputData):
    def TestSum(self, i):
        self.assertEqual(self.x1 + self.y1, 6)


