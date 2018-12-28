import unittest


class MyClass:
    def __init__(self, foo):
        if foo != 1:
            raise ValueError("foo is not equal to 1!")


class MyClass2:
    def __init__(self):
        pass


class TestFoo(unittest.TestCase):
    def testInsufficientArgs(self):
        foo = 0
        self.assertRaises(ValueError, MyClass, foo)

    def testArgs(self):
        self.assertRaises(TypeError, MyClass2, ("fsa", "fds"))


if __name__ == '__main__':
    unittest.main()

# class TestUm(unittest.TestCase):
#
#     def testAssertTrue(self):
#         """Causes an error if the value of the argument !=True"""
#         self.assertTrue(True)
#
#     def testFailUnless(self):
#         """Old name for assertTrue()
#         Causes an error if the value of the argument !=True"""
#         self.failUnless(True)
#
#     def testFailIf(self):
#         """Old function, now called assertFalse()"""
#         self.failIf(False)
#
#     def testAssertFalse(self):
#         """If the value of the argument !=False, then throws an error"""
#         self.assertFalse(False)
#
#     def testEqual(self):
#         """Check whether two arguments are equal"""
#         self.failUnlessEqual(1, 3 - 2)
#
#     def testNotEqual(self):
#         """Checking NOT equality of two arguments"""
#         self.failIfEqual(2, 3 - 2)
#
#     def testEqualFail(self):
#         """Swears if the value of arguments is equal each other"""
#         self.failIfEqual(1, 2)
#
#     def testNotEqualFail(self):
#         """Swears if the argument value is not equal"""
#         self.failUnlessEqual(2, 3 - 1)
#
#     def testNotAlmostEqual(self):
#         """The old name of the function.
#         Now called assertNotAlmostEqual()
#         Compares two arguments with rounding, you can set this rounding.
#         Swears if values are equal"""
#         self.failIfAlmostEqual(1.1, 3.3 - 2.0, places=1)
#
#     def testAlmostEqual(self):
#         """Old function name
#         Now called assertAlmostEqual()
#         Compares two arguments with rounding, you can set this rounding
#         Swears if value are not equal"""
#
#
# if __name__ == '__main__':
#     unittest.main()

# class TestUm(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass
#
#     def test_numbers_3_4(self):
#         self.assertEqual(3 * 4, 12)
#
#     def test_strings_a_3(self):
#         self.assertEqual('a' * 3, 'aaa')
#
#
# if __name__ == '__main__':
#     unittest.main()
