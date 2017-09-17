#Dice Program
from random import randint

while True:
  roll = raw_input("Press Enter To Roll!")
  if roll == "":
    q = randint(1,6)
    print ("Result is: {0}".format(q))
    print
  else:
    print("Invalid Input, Try Again")
    print