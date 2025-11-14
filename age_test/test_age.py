import unittest
from age import test_age

class TestAge(unittest.TestCase):
    def test_age(self):
        self.assertEqual(test_age(0), "child")
        self.assertEqual(test_age(9), "child")
        self.assertEqual(test_age(10), "teenager")
        self.assertEqual(test_age(17), "teenager")
        self.assertEqual(test_age(18), "adult")
        self.assertEqual(test_age(65), "adult")
        self.assertEqual(test_age(66), "golden age")
        self.assertEqual(test_age(125), "golden age")
        self.assertEqual(test_age(126), "126 is not a valid age")
