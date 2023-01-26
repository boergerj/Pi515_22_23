def add(x, y):
  return x + y


def sub(x, y):
  return x - y


def power(x, y):
  """return x to the power of y"""
  answer = 1
  for p in range(y):
    answer *= x
  return answer


if __name__ == '__main__':
  print("3 + 4 = ", add(3, 4))
  print("3 - 4 = ", sub(3, 4))
  print("3 ** 4 = ", power(3, 4))