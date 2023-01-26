import unittest
import calculator


class TestCalculator(unittest.TestCase):

  def test_add(self):
    assert calculator.add(1, 2) == 3

  def test_sub(self):
    assert calculator.sub(4, 1) == 3
    self.assertEqual(3, calculator.sub(4, 1))

  def test_power(self):
    self.assertEqual(8, calculator.power(2, 3))


if __name__ == '__main__':
  unittest.main(verbosity=2)
