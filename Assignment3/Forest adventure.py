print("Welcome to the Forest Adventure!")
path = input("Do you want to go 'left' or 'right'? ")

if path == "left":
    action = input("Do you want to 'explore' or 'rest'? ")
    
    if action == "explore":
        print("You found treasure!")
    elif action == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("You chose a dangerous path and got lost. Game Over.")
