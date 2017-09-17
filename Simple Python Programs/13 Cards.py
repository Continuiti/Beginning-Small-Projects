from random import randint

while True:
  inp = input("")

  x = randint(1,13)
  y = randint(1,13)

  if inp == "1":
   x = randint(8,12)
   y = randint(1,8)

  if inp == "2":
    x = randint(1,6)
    y = randint(6,13)


  print("First Number: {0}".format(x))
  print("Second Number: {0}".format(y))
  print("")