import unittest
from Assignment5 import fahrenheit_to_celsius, fibonacci

class TestAssignment5(unittest.TestCase):

    def test_fahrenheit_to_celsius_valid(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=1)

    def test_fahrenheit_to_celsius_invalid_type(self):
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("100")

    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_general_cases(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_invalid_type(self):
        with self.assertRaises(TypeError):
            fibonacci(3.5)

if __name__ == '__main__':
    unittest.main()
