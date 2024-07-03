print("Welcome to the quest of finding the One-Piece Treasure presented by S.H.ShUvo Ahmed")
"\n"
print("Your mission is to find the most desirable one-piece. Pirates have been searching it for thousands of years!")
"\n"

choice1 = input("Which way you would like to go? Type 'left' or 'right' ").lower()

if choice1 == "left":
#Game will continue
   choice2 = input("What would you like to do next? Type 'swim' or 'wait' ").lower()

   if choice2 == "wait":
       #Game will continue

       choice3 = input("Which door would you open? Choose among 'Red' , 'Blue' or 'Yellow' ").lower()

       if choice3 == "red":
           print("You've been burned by fire. Game Over!")
       elif choice3 == "blue":
           print("You've eaten by beasts. Game Over!")
       elif choice3 == "yellow":
           print("Congratulations! You've finally found the ONE-PIECE!")
       else:
           print("Game Over!")
   else:
       print("You\'ve been attacked by an angry shark. Game Over!")

else:
    print('You\'ve just fell into a hole. Game Over!')


