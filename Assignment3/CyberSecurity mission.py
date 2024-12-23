print("Welcome to the Cybersecurity Mission!")

choice1 = input("Do you want to 'trace the hacker' or 'secure the system'? ")

if choice1 == "trace the hacker":
    choice2 = input("Do you want to 'track their IP' or 'decode their message'? ")
    if choice2 == "track their IP":
        print("You caught the hacker. You Win!")
    elif choice2 == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif choice1 == "secure the system":
    choice2 = input("Do you want to 'shut down the server' or 'upgrade the firewall'? ")
    if choice2 == "shut down the server":
        print("The attack was stopped. You Win!")
    elif choice2 == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
