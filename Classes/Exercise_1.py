# Create a class for contact information
# Use the included Template.py as reference

# 1. Define a class called contact
# 2. Write the constructor
# 3. Create instance variables for the following:
#   - First name (argument 1)
#   - Last name (argument 2)
#   - Phone number (argument 3)
#   - Blocked status  (default false)
# 4. Create an instance method which changes
# the blocked status from false to true

class contact:
  isBlocked = False

  def __init__(self,first,last,phonenum):
    self.firstname = first
    self.lastname = last
    self.phone = phonenum
  
  def toggleBlocked(self):
    if self.isBlocked:
      self.isBlocked = False
    else:
      self.isBlocked = True

  
x = contact('Joel','Aguirre','123')
print(x.firstname)
print(x.lastname)
print(x.phone)
print(x.isBlocked)
x.toggleBlocked()
print(x.isBlocked)
x.toggleBlocked()
print(x.isBlocked)