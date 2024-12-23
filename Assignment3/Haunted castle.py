print("Welcome to the Haunted Castle!")
choice1 = input("Do you want to 'enter the castle' or 'run away'? ")
if choice1 == "enter the castle":
    choice2 = input("Choose a door: 'red', 'green', or 'black': ")
    if choice2 == "red":
        print("You entered a room full of flames. Game Over.")
    elif choice2 == "green":
        print("You found the treasure. You Win!")
    elif choice2 == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice1 == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice. Game Over.")
