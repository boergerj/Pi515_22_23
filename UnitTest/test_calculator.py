import pytest
from calculator import Calculator


# similar to unittest style
class TestCalculator:

  def test_add(self):
    test_add()


# simplified style
def test_add():
  cal = Calculator()
  assert 3 == cal.add(1, 2)


# fixture to instantiate a calculator
def test_sub(cal):
  assert 3 == cal.sub(5, 2)


def test_mul(cal):
  assert 4 == cal.mul(2, 4)


def test_div_normal(cal):
  assert 2 == cal.div(4, 2)


def test_div(cal):
  with pytest.raises(ZeroDivisionError):
    cal.div(1, 0)


# fixture in pytest
@pytest.fixture
def cal():
  return Calculator()


if __name__ == '__main__':
  pytest.main(args=["-v"])
