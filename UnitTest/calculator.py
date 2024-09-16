from reader import Reader


class Calculator:
  """A simple integer calculator."""

  def __init__(self):
    self.reader = Reader()
    self.commands = {
      '+': self.add,
      '-': self.sub,
      '*': self.mul,
      '/': self.div,
      '^': self.power
    }

  # just to make patching easier
  def get_input(self, prompt):
    return input(prompt)

  def add(self, x, y):
    return x + y

  def sub(self, x, y):
    return x - y

  def mul(self, x, y):
    return x * y

  def div(self, x, y):
    return x / y

  def power(self, x, y):
    """return x to the power of y"""
    if y == 1: return x
    else:
      result = x * self.power(x, y - 1)
      return result

  def loop(self):
    while True:
      cmdString = self.get_input("> ")
      cmd = self.reader.read(cmdString)
      if cmd and len(cmd) == 3:
        result = self.commands[cmd[0]](cmd[1], cmd[2])
        print(result)
      elif cmd and cmd[0] == 'q':
        return
      else:
        print(f"{cmdString} is not recognized")


if __name__ == '__main__':  # pragma: no cover
  cal = Calculator()
  print("3 + 4 = ", cal.add(3, 4))
  print("3 - 4 = ", cal.sub(3, 4))
  print("3 ** 4 = ", cal.power(3, 4))
