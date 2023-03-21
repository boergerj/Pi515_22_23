from calculator import Calculator
from unittest.mock import MagicMock

mockAdd = MagicMock(name='add')
mockAdd.return_value = 5

cal = Calculator()
cal.add = mockAdd

print(cal.add(1, 2))
print(cal.add(3, 4))