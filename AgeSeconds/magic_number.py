from random import randint

def check():
  magic_number = randint(1,10)
  user_guess = int(input("Guess a random number between 1 and 10:"))
  print("Magic Number: {}".format(magic_number))
  return magic_number == user_guess

def guess():
  correct = False
  while correct == False:
    correct = check()

guess()
