##Black Jack Game is basically about cards , cards include Queen ,King, and Joker all with a value of 10 and 
## Diamonds,Hearts and Spades etc when you start the game two cards of User(Players) can be seen and the computer displays  
## only one card and  other card is not displayed out of two cards and two options are provided firsty ADD  
## a card and Show the cards (Stand) type Yes  You can add Cards as much you can but the value should be less than 22,
#.If the total is 21 after you show the card you win the game 
## and vice-versa.If the value of COMPUTER is more than USER and less than 22 the Computer(Dealer) wins the 
## Game and Vice-versa.
Start = input("Lets Play BlackJack Game Type,YES or NO ").lower()

while Start == "yes":
        print("BLACK JACK GAME.")
        import os
        from time import sleep
        import random
        Cards = [2,3,4,5,6,7,8,9,10,10,10,10,11,1]    # THESE ARE ALL THE CARD NUMBERS ,10 = QUEEN OR KING or JOKER OR "A" and 1 an be  "A" also.
        a = 0
        b = 0
        User =  [Cards[random.randint(0,11)],Cards[random.randint(0,11)]]
        Computer  = [ Cards[random.randint(0,11)],Cards[random.randint(0,11)]]
        Computer_Cards = Computer[random.randint(0,1)]
        print (f"User[{User[0]},{User[1]}]  Total User =  {User[0] + User[1]}")
        print(f"Dealers[{Computer_Cards},Hidden Card] Total Dealers = {Computer_Cards}")
        a = 0
        b = 0
        c = 0
        d = 0
        v = 0
        x = 0
        i = random.randint(1,11)
        Add_Cards1 = random.randint(0,1)
        g = random.randint(1,11)

        Add_Cards = input("If you want to add cards,Type Add or Type No ").lower()

        if  Add_Cards == "no":
                Stand = input("Do you want to stand,Type yes ").lower()              
                #Computer.append(Cards[random.randint(0,11)])
                Stand = Stand
                
                if Stand == "yes":
                        for Card in User:
                                a = a + Card
                        print("User",User,"Total players =",a)
                        for Card1 in Computer:
                                b = b + Card1
                        if b<17:
                                while b < 17:
                                        i = random.randint(1,11)
                                        Computer.append(i)


                                        b = b + i

                        print("Computer",Computer,"Total Dealers = ",b)
                        
                        if a == 21:
                                print("Blackjack, The user won the Game.")
                                print("The Dealer lose the Game.")
                        elif b == 21:
                                print("Blackjack,The Dealer won the Game.")
                                print("The User lose the Game.")
                        elif  a < 22 and (a > b or b < a or b > 21) :
                                print("The user  won the Game.")
                                print("The Dealer lose the Game.")
                        elif b < 22 and (b>a or a>b or a > 21) :
                                print("The Dealer  won the Game.")
                                print("The user lose the Game.")
                            
                        elif (a == b or b == a) and (a < 22 and b < 22):
                                print("Match Drawn.")


        elif Add_Cards == "add":
                for Card in User:
                        a = a + Card
                if a<20:
                         x = random.randint(1,11)
                         User.append(x)
                        
                               
                         a = a + x   
                print("User",User,"Total players =",a)
                if a > 21:
                         for Card1 in Computer:
                                b = b + Card1
                         print("Computer",Computer,"Total Dealers = ",b)
                         print("The Dealer  won the Game")
                         print("The user lose the Game")
                elif a<21:        
                        Stand = input("Do you want to stand,Type yes ").lower()

                        if Stand == "yes":
                                for Card1 in Computer:
                                        b = b + Card1
                                if b<17:
                                        while b<17:
                                                v = random.randint(1,11)
                                                Computer.append(v)
                                                b = b + v
                                print("Computer",Computer,"Total Dealers = ",b)

                                if a == 21:
                                      print("Blackjack, The user won the Game.")
                                      print("The Dealer Lose the Game.")
                                elif b == 21:
                                       print("Blackjack,The Dealer won the Game.")
                                       print("The User Lose the Game.")
                                elif  a < 22 and (a > b or b < a or b > 21) :
                                     print("The user  won the Game")
                                     print("The Dealer lose the Game.")
                                elif b < 22 and (b>a or a>b or a > 21) :
                                       print("The Dealer  won the Game")
                                       print("The user lose the Game")
                                   
                                elif (a == b or b == a) and (a < 22 and b < 22):
                                      print("Match Drawn")



                                                


                        elif Stand == "no":
                                
                                while Stand == "no":
                                        Add_Cards = input("If you want to add cards,Type Add or Type No ").lower()
                                        
                                        a = 0
                                        if Add_Cards == "add":
                                                for Card in User:
                                                        a = a + Card
                                                if a<20:
                                                        x = random.randint(1,11)
                                                        User.append(x)
                                                        
                                                               
                                                        a = a + x   
                                                print("User",User,"Total players =",a)
                                                if a > 21:
                                                         for Card1 in Computer:
                                                                b = b + Card1
                                                         print("Computer",Computer,"Total Dealers = ",b)
                                                         print("The Dealer  won the Game")
                                                         print("The user lose the Game")
                                                if a<21:
                                                        Stand = input("Do you want to stand,Type yes ").lower()
                                                        if Stand == "yes":
                                                                for Card1 in Computer:
                                                                        b = b + Card1
                                                                if b<17:
                                                                        while b < 17:
                                                                                v = random.randint(1,11)
                                                                                Computer.append(v)
                                                                                b = b + v
                                                                print("Computer",Computer,"Total Dealers = ",b)
                                                                if a == 21:
                                                                        print("Blackjack, The user won the Game.")
                                                                        print("The Dealer Lose the Game.")
                                                                elif b == 21:
                                                                        print("Blackjack,The Dealer won the Game.")
                                                                        print("The User Lose the Game.")
                                                                elif  a < 22 and (a > b or b < a or b > 21) :
                                                                        print("The user  won the Game")
                                                                        print("The Dealer lose the Game.")
                                                                elif b < 22 and (b>a or a>b or a > 21) :
                                                                        print("The Dealer  won the Game")
                                                                        print("The user lose the Game")
                                                                    
                                                                elif (a == b or b == a) and (a < 22 and b < 22):
                                                                        print("Match Drawn")
                                                                                                                                                

                                                elif a == 21:
                                                        print("Blackjack, The user won the Game.")
                                                        print("The Dealer lose the Game.")

                                                elif a>21:
                                                 break

                elif a == 21:
                        print("Blackjack, The user won the Game.")
                        print("The Dealer lose the Game.")

        sleep(5)
        os.syatem('cls')
        
        Start = input("Do you wanna  Play BlackJack Game Again ,Type YES or NO ").lower()


                                                                                           
                                        









                        
                        






                        


