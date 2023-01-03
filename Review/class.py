class Plant:
  name = "plant" # class variable

  def __init__(self):
    self.height = 0 # instance variable

  def grow(self):
    pass

  @classmethod
  def rename(cls, new_name):
    cls.name = new_name

  @staticmethod
  def add(a, b):
    return a + b
  
  def __repr__(self):
    return f"Name: {self.name}, Height: {self.height}"

class Grass(Plant):
  name = "grass"
  def grow(self):
    self.height += 2

class Corn(Plant):
  name = "corn"
  def grow(self):
    self.height += 1


if __name__ == "__main__":
  p1 = Plant()
  p2 = Grass()
  p3 = Corn()
  p4 = Corn()
  
  p2.grow()
  p3.grow()

  print(p1)
  print(p2)
  print(p3)
  print(p4)

  # class method
  p3.rename("hybrid")
  print(p3)
  print(p4)

  # static method
  print(p1.add(3, 4))