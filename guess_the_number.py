import random

points = 0
MaxumNumber = 9
currentTryes = 0
RandomizedNumber = random.randint(0,MaxumNumber)

while True:
  try:
    userInput = int(input("\nyour points: {} \nGuess number between {} - {} > ".format(points,0,MaxumNumber)))
    if currentTryes < 3 and userInput != RandomizedNumber:
      currentTryes += 1
      print("you have {} tryes left before you loose points".format(4 - currentTryes))
      if userInput > RandomizedNumber:
        print("guess lower")
      elif userInput < RandomizedNumber:
        print("guess higher")
    elif currentTryes == 3 and userInput != RandomizedNumber:
      if points > 0:
        points -= 1
        print("you current points is now {}".format(points))
      else:
        print("sorry you lost the game")
    else:
      points += 1
      print("correct! The number was {} \n points {}".format(RandomizedNumber,points))
      RandomizedNumber = random.randint(0,MaxumNumber)
      currentTryes = 0
      MaxumNumber *= 2
  except ValueError:
    print("sorry, your input is not a number")
