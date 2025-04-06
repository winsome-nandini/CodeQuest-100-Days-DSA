# Day 6: The Path of Decision

while True:
    choice = input("Which path do you choose? (left/right): ").lower()
    if choice == "left":
        print("You found a hidden tunnel! You're safe.")
        break
    elif choice == "right":
        print("Oh no! The Glitch's trap was here! Try again.")
        break
    else:
        print("Invalid choice Please enter 'left' or 'right'.")