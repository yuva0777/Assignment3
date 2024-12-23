print("Welcome to the Pirate Ship Adventure!")
choice1 = input("Do you want to 'search for treasure' or 'battle enemy ships'? ")
if choice1 == "search for treasure":
    choice2 = input("Do you want to 'dig on the island' or 'explore the cave'? ")
    if choice2 == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif choice2 == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice1 == "battle enemy ships":
    choice2 = input("Do you want to 'attack' or 'defend'? ")
    if choice2 == "attack":
        print("You won the battle. You Win!")
    elif choice2 == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
