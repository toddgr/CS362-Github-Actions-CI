"""
test file
"""


import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)
        self.assertEqual(example.add(5, 2), 7)
        self.assertEqual(example.add(13, 5), 18)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(1, 1), 0)
        self.assertEqual(example.subtract(13, 7), 6)
        self.assertEqual(example.subtract(20, 5), 15)

    def test_multiply_1(self):
        self.assertEqual(example.multiply(3, 4), 12)
        self.assertEqual(example.multiply(20, 5), 100)
        self.assertEqual(example.multiply(9, 6), 54)

    def test_divide_1(self):
        self.assertEqual(example.divide(12, 3), 4)
        self.assertEqual(example.divide(45, 5), 9)
        self.assertEqual(example.divide(400, 100), 4)


if __name__ == '__main__':
    unittest.main()
