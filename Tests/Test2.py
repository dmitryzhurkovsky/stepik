import unittest


class TestUM(unittest.TestCase):

    def testAssertTrue(self):
        """
        Call error if argument's value's != True
        :return:
        """
        self.assertTrue(True)

    def testFailUnless(self):
        """
        Old name for assertTrue()
        Call error if argument's value's != True
        :return:
        """

        self.failUnless(True)

    def testFailIf(self):
        """
        It's old function, it's call assertFalse() at the moment.
        :return:
        """
        self.failIf(False)

    def testAssertFalse(self):
        """
        If argument's value is != False, then return error.
        :return:
        """
        self.assertFalse(False)

    def testEqual(self):
        """
        Checking equality 2 arguments
        :return:
        """
        self.failUnlessEqual(1, 3 - 2)

    def testNotEqual(self):
        """
        Checking no equality 2 arguments
        :return:
        """
        self.failIfEqual(2, 3 - 2)

    def testEqualFail(self):
        """
        Swears if the arguments value is
        :return:
        """
        self.failIfEqual(1, 2)

    def testNotEqualFail(self):
        """
        Swears if the arguments value isn't
        :return:
        """
        self.failUnlessEqual(2, 3 - 1)

    def testNotAlmostEqual(self):
        """
        It is old name function.
        Now it's assertNotAlmostEqual()
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения равны
        :return:
        """
        self.failIfAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def testAlmostEqual(self):
        """
        Старое название функции
        Теперь называется assertAlmostEqual()
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения не равны
        :return:
        """
        self.failUnlessAlmostEqual(1.1, 3.3 - 2.0, places=0)

    if __name__ == '__main__':
        unittest.main()