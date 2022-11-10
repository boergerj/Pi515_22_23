# Copyright 2022 PI515

import random

keepAsking = True
while keepAsking:
    num = input('Type a number for an upper bound: ')
    if num.isdigit():
        print("Let's play!")
        num = int(num)
        # something about the loop condition
    else:
        print("Invalid input. Try again.")

secret = random.randint(1, num)
guess = None
count = 1

while guess != secret:
    guess = input("Type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)
    if False: # can't always be wrong
        print("You got it!")
    else:
        print("Try again.")
        # what else?

if count == 1:
    print("It took you", count, "guess!")
else:
    print("It took you", count, "guesses!")
