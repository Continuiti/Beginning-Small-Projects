import random
x = 6

Elements = ["Elephant", "Giraffe", "Dog", "Cat", "Bird", "Horse", "Cow", "Pig"]
answer = random.choice(Elements)

while True:
  inp = input("Pick a letter: ")
  
  if inp in answer:
    print("Correct, letter {0} is in answer.".format(inp))
    print("")
  else:
    x = x - 1
    if x > 1:
      print("Wrong, {0} chances left.".format(x))
    if x == 1:
      print("Wrong, final chance.")
    print()
    if x == 0:
      print("You Lose.")
      print("The answer was: {0}".format(answer))
      print("")
      break