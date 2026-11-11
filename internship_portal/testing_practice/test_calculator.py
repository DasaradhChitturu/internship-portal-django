import unittest

def calculate_total(price, quantity):
    return price * quantity


class TestCalculator(unittest.TestCase):

    def test_calculate_total(self):
          result = calculate_total(200, 4)
          self.assertEqual(result, 800)

    def test_zero_quantity(self):
            result = calculate_total(200, 0)
            self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()