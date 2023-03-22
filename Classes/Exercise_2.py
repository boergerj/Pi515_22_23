# Create a class to hold your contact list
# 1. Define a class called contactList
# 2. Create a class variable list
# 3. Create an instance method called printList()
#  to print class variable list

# 4. Below your class definition, create a
#  new instance of contactList
# 5. Create 2 contacts and add them to list
#  inside your contactList object
# 6. Run your instance method printList()


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

class contactList:
  def __init__(self):
    self.list = []

  def printList(self):
    for i in self.list:
      print(i.firstname,i.lastName)
  
jordan = contact("Jordan","Boerger","123")

matt = contact("Matt","O","456")

addressBook = contactList()
addressBook.list.append(jordan)
addressBook.list.append(matt)
addressBook.printList()
