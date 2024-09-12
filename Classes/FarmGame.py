# import modules
import os
import random

# Clears shell terminal
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# Contains information about the player
class Player:

  def __init__(self, name):
    self.name = name
    self.score = 0

class Crop:
  name = ""
  score = 0
  pic = "\|/"

class Wheat(Crop):
  def __init__ (self):
    self.name = "Wheat"
    self.score = 10
    
class RagWeed(Crop):
  def __init__ (self):
    self.name = "Rag Weed"
    self.score = -5
  

# Program Start
# Player enters name
playerName = input('Please enter your name\n')
p1 = Player(playerName)
print('Welcome ' + p1.name + '! Let\'s start farming!')

# Press key to enter game
input('Press any key to continue...')
clear()

userIn = ''
# Game loop
while userIn != 'quit' and userIn != 'q':
  # Print player info at top of screen
  print(p1.name)
  print("Score: ", p1.score)

  randNum = random.randint(0,1)

  if randNum == 0:
    plantObj = Wheat()
  elif randNum == 1:
    plantObj = RagWeed()
  
  # Print plant information
  print('Plant: ',plantObj.name)
  print(plantObj.pic)
  print("\n")

  # Print commands available to user
  print('Commands:')
  print('harvest / h - harvest current plant')
  print('spray / s - spray plant with herbicide')
  print('quit / q - quit game')
  print('\n')

  # Execute command on user input
  userIn = input('Input: ')
  if userIn == 'harvest' or userIn == 'h':
    p1.score += plantObj.score
  elif userIn == 'spray' or userIn == 's':
    pass
  else:
    print('Invalid command')

  # Clear terminal
  clear()
