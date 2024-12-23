print("Welcome to the Jungle Survival Challenge!")
choice1 = input("Do you want to 'search for food' or 'build a shelter'? ")
if choice1 == "search for food":
    choice2 = input("Do you want to 'hunt' or 'gather'? ")
    if choice2 == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice2 == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Game Over.")
elif choice1 == "build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid choice. Game Over.")
