import re


class Reader:
  """Use regular expression to read a simple math command.
  
  Examples of supported commands:
  1 + 2
  5 - 3
  2 * 4
  6 / 2
  3 ^ 2
  """

  calculatorPattern = "([0-9]+)\s*([+\-*/^])\s*([0-9]+)|([qQ]).*"

  def __init__(self):
    self.pattern = re.compile(self.calculatorPattern)

  def read(self, command):
    m = self.pattern.match(command)

    if m and not m.group(4):
      return m.group(2), int(m.group(1)), int(m.group(3))
    elif m:
      return m.group(4).lower()
    else:
      return None


if __name__ == '__main__':
  p = Reader()
  print(p.read("3+5"))
  print(p.read("3 - 5"))
  print(p.read("quit"))