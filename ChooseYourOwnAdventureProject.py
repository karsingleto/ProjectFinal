name = input("Type your name: ")
print("Welcome", name, "to a Middle-Earth adventure!")

answer = input(
    "A wise wizard shows up at your doorstep, invites you to come alongside him to destroy a ring, do you decline or accept? ").lower()

if answer == "decline":
    answer = input(
        "With strong distaste for the silly wizard, you decline his offer, would you like to stay at home or take a walk (stay/walk)? ")

    if answer == "stay":
        print("You stay at home. The following morning your home is raided by evil goblins.")
    elif answer == "walk":
        print("You go for a walk and are found and eaten by an evil goblin.")
    else:
        print('Not a valid option. You lose.')

elif answer == "accept":
    answer = input(
        "You go along with the wizard, you come to a bridge, it is patchy and the rope is tattered, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("The wise wizard continues on. You go back and are crushed by the foot of a large giant.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and have found the pit of boiling lava. Do you drop the ring into the lava as suggested by the wise wizard (yes/no)? ")

        if answer == "yes":
            print("You drop the ring in the melting lava, defeating the powers of darkness forever. You WIN!")
        elif answer == "no":
            print("You keep the ring and a small creature kills you for it. You lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for participating in a Middle-Earth Adventure", name)
