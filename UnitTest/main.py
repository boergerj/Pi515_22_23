from calculator import Calculator
from reader import Reader

if __name__ == '__main__':
  cal = Calculator()
  print("3 + 4 = ", cal.add(3, 4))
  print("3 - 4 = ", cal.sub(3, 4))
  print("3 ** 4 = ", cal.power(3, 4))

  cal.loop()