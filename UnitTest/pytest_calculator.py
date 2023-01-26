import pytest
import calculator


def test_add():
  assert 3 == calculator.add(1, 2)
