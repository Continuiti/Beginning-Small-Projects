#Mini Project 3 
#Black Jack - 0.5% House Edge

import random
from random import randint


d = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
e = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


#Computer
while True:
  picke1 = random.choice(d)
  picke2 = random.choice(d)

  print ("Opponent pulled '{0}' and 'Hidden Card'".format(picke1))

  if picke1 == "Jack" or picke1 == "Queen" or picke1 == "King":
    nume1 = 10
  elif picke1 == "Ace":
    nume1 = 11
  else:
    nume1 = int(picke1)

#Define Second Number
  if picke2 == "Jack" or picke2 == "Queen" or picke2 == "King":
    nume2 = 10
  elif picke2 == "Ace":
    nume2 = 11
  else:
    nume2 = int(picke2)

  numt = nume1 + nume2

  while numt < 16:
    numt = numt + nume1
    print("Opponent Draws A Card")
    if numt > 21:
      print("Opponent Busted.")
      quit()
  
  else:
   print("Opponent Stays")
   print("")
   print("--------------------------")
   break

#--------------------------------------------------------------------------#

#Player
while True:
#Pull Random Number 
  g = random.choice(d)
  gg = random.choice(d)

  print("You pulled '{0}' and '{1}'".format(g, gg))

#Define Second Number
  if g == "Jack" or g == "Queen" or g == "King":
    num1 = 10
  elif g == "Ace":
    num1 = 11
  else:
    num1 = int(g)

#Define Second Number
  if gg == "Jack" or gg == "Queen" or gg == "King":
    num2 = 10
  elif gg == "Ace":
    num2 = 11
  else:
    num2 = int(gg)
    
  
  ddog = (num1 + num2)

  print("Your Current Score Is: {0}".format(ddog))
  print("--------------------------")
  print("")
  break

if ddog == 21:
  print("")
  print("You Got Blackjack!")
  quit()
  
  
while True: 
  print("")
  print("")
  inp = input("Hit or Stay?")
  
  x = random.choice(e)
  
  if x == "Jack" or x == "Queen" or x == "King":
    numq1 = 10
  
  elif x == "Ace":
    if ddog == 11:
      numq1 = 10
    elif ddog == 10:
      numq1 = 11
    elif ddog > 11:
      numq1 = 1
    else:
      numq1 = 11

  else:
    numq1 = int(x)

  if inp == "stay" or inp == "Stay" or inp == " ":
    break
  elif inp == "hit" or inp == "Hit" or inp == "":
    print("--------------------------")
    print("You pulled '{0}'".format(x))
    ddog = ddog + numq1
    print("Your Current Score Is: {0}".format(ddog))
    print("--------------------------")
    if ddog > 21:
      print("")
      print("You Busted.")
      quit()
  
if ddog > numt:
  print("")
  print("Opponent Had: {0}".format(numt))
  print("You Won!")
elif numt > ddog:
  print("")
  print("Opponent Won With {0} Points.".format(numt))

  
  
  
  
  
  
  
  
  
  