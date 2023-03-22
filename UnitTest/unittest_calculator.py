import unittest
import calculator
from unittest.mock import patch


class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.cal = calculator.Calculator()

  def tearDown(self):
    # cleaning up
    pass

  def test_add(self):
    # assert evaluate true or false
    assert self.cal.add(1, 2) == 3

  def test_sub(self):
    assert self.cal.sub(4, 1) == 3

    # alternative assertion
    self.assertEqual(3, self.cal.sub(4, 1))

  def test_mul(self):
    # common pattern:
    # Arrange-Act-Assert
    num1 = 3
    num2 = 4
    expected = num1 * num2

    actual = self.cal.mul(num1, num2)

    self.assertEqual(expected, actual)

  def test_power(self):
    self.assertEqual(8, self.cal.power(2, 3))

  # check for exceptions; note the div call is passed as a callable
  def test_divided_by_zero(self):
    self.assertRaises(ZeroDivisionError, self.cal.div, 1, 0)

  # loop requires user input
  @patch("calculator.Calculator.get_input", return_value="quit")
  def test_loop_would_stop(self, mockInput):
    self.cal.loop()


if __name__ == '__main__':
  unittest.main(verbosity=2)
