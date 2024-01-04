# Guess number game is basically about Guess a number between 1 to 100 ,For easy Game you Get 10 chances to Guess the Correct number.
#For Hard Game you get 5 chances to Guess the correct number.
Start = "yes"
while Start == "yes":
    import os
    from time import sleep
    import random
    Correct_Number = random.randint(2,99)
    print(Correct_Number)
    print("Number Guessing Game")

    Game = input("Hard or Easy ").lower()
    if Game == "easy":
        print("You have 10 chances to Guess a number.")
    elif Game == "hard":
      print("You have 5 chances to Guess a number.")

    i = 1

    while (i<=10 and Game == "easy")  or (i<=5 and Game == "hard"):
      
      Guess_number = int(input("Guess  a number between 1 to 100 "))
      
      if Guess_number > Correct_Number:
        print("The  Guess Number is too High.")
      elif Guess_number < Correct_Number:
        print("The  Guess Number is too Low.")
      elif Guess_number == Correct_Number:
          
        print("Correct Guess,You Won the Game.")
        break

      i = i+1
      Game = Game
      if (i == 6 and Game == "hard")or (i == 11 and Game == "easy"):
          print("You Lose the Game")
    sleep(5)
    os.system('clear')
    Start = input("Do you want to Start the game again,Type Yes or No ").lower()
