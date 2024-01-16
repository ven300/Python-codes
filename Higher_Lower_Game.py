# Higher Lower Game is Basically about Guessing the number of followers between celebrity or sportsperson or vice-versa or between celebrity and famous areas.
# And the average score is bascically 3.

from data import data

import random

print("HIGHER LOWER GAME")
print("\n")

random_number1 = random.randint(0,49)
Game_Again = "yes"
while Game_Again == "yes":
    a = 0
    random_number1 = random.randint(0,49)
    print(f"name:-{data[random_number1]['name']}\nfollower_count:-{data[random_number1]['follower_count']}\ndescription:-{data[random_number1]['description']}\ncountry:-{data[random_number1]['country']}")
    print("\n")
    Game = "Continue"
    while Game == "Continue":
        import os
        from time import sleep
        list1 = []
        random_number2 = random.randint(0,49)
        print('VS')
        print("\n")
        print(f"name:-{data[random_number2]['name']}\ndescription:-{data[random_number2]['description']}\ncountry:-{data[random_number2]['country']}")
        Followers = input(f"Number of Followers of {data[random_number2]['name']} are Higher or Lower ").lower() #Basically to Guess the Number of followers
        print("Follower Count =",data[random_number2]['follower_count'])
        if (Followers == "higher" or Followers == "lower")  and data[random_number1]['follower_count'] == data[random_number2]['follower_count']:
            list1.append(1)
            a=a
            for points in list1:
                i=a+1
                a = i
            print("Points = ",a)
            Game = "Continue"
            
        
        if Followers == "higher" and data[random_number1]['follower_count'] < data[random_number2]['follower_count']:
            list1.append(1)
            a= a
            for points in list1:
                i=a+1
                a = i
            print("Points = ",a)
            Game = "Continue"
        if  Followers == "lower" and data[random_number1]['follower_count'] > data[random_number2]['follower_count']:
            list1.append(1)
            a= a
            for points in list1:
                i=a+1
                a = i
            print("Points = ",a)
            Game = "Continue"
        score = a
        if Followers == "lower" and data[random_number1]['follower_count'] < data[random_number2]['follower_count']:
            print(data[random_number1]['follower_count'])
            Game = "Stop"
        if Followers == "higher" and data[random_number1]['follower_count'] > data[random_number2]['follower_count']:
            Game = "Stop"
        if score<3 and Game == 'Stop' and (Followers == "higher" or Followers == "lower"):
            print(score,"is not a good score","Average score is 3.")
        if score == 3 and Game == 'Stop' and (Followers == "higher" or Followers == "lower"):
            print(score,"is just a average score.")
        if score > 3 and Game == 'Stop'  and (Followers == "higher" or Followers == "lower"):
            print(score,"is a GOOD score.")
        sleep(5)
        os.system('cls')

        
        if a> 0 and Game =='Continue':
            print("HIGHER LOWER GAME")
            print("\n")
            print("score =",a)
        
        if Game =="Continue" and (Followers == "lower" or Followers == "higher"):
            print(f"name:-{data[random_number2]['name']}\nfollower_count:-{data[random_number2]['follower_count']}\ndescription:-{data[random_number2]['description']}\ncountry:-{data[random_number2]['country']}")
            random_number1 = random_number2
        if Game == 'Continue':
            print("\n")
            
        Game = Game
        if Game == "Stop":
            print("HIGHER LOWER GAME")
            print("\n")
            Game_Again = input("Do you want to Play the game again,Type Yes or no ").lower()



