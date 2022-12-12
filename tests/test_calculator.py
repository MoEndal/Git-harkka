import unittest
from ..src import calculator as calculator
#asra
# import src.calculator as calculator

class TestCalculator(unittest.TestCase):

    def test_plus(self):
        result = calculator.plus(2, 3)
        self.assertEqual(result, 5)

    def test_plus_works_with_negative_numbers(self):
        result = calculator.plus(-2, -3)
        self.assertEqual(result, -5)
    
    def test_plus_returns_sum_of_floats(self):
        result = calculator.plus(2.4, 3.2)
        self.assertEqual(result, 5.6)

    def test_plus_returns_sum_of_integer_and_float(self):
        result = calculator.plus(2, 3.2)
        self.assertEqual(result, 5.2)

    def test_plus_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.plus(1, "a")

    def test_minus(self):
        result = calculator.minus(2, 3)
        self.assertEqual(result, -1)

    def test_minus_negative(self):
        result = calculator.minus(-2, -3)
        self.assertEqual(result, 1)
    
    def test_minus_floats(self):
        result = calculator.minus(2.4, 3.2)
        self.assertAlmostEqual(result, -0.8)

    def test_minus_integar_and_float(self):
        result = calculator.minus(2, 3.2)
        self.assertAlmostEqual(result, -1.2)

    def test_minus_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.minus(1, "a")
    
    def test_jako(self):
        result = calculator.jako(2, 3)
        self.assertGreaterEqual(result, 0.6)

    # def test_minus_negative(self):
    #     result = calculator.minus(-2, -3)
    #     self.assertEqual(result, 1)
    
    # def test_minus_floats(self):
    #     result = calculator.minus(2.4, 3.2)
    #     self.assertAlmostEqual(result, -0.8)

    # def test_minus_integar_and_float(self):
    #     result = calculator.minus(2, 3.2)
    #     self.assertAlmostEqual(result, -1.2)

    # def test_minus_error_if_parameters_are_not_numbers(self):
    #     with self.assertRaises(TypeError):
    #         calculator.minus(1, "a")  

