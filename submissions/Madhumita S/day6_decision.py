a = input("Which path do you choose? (left/right):")
while(1):
    if(a.lower()=="left"):
        print("You found a hidden tunnel! You’re safe. 🚀")
        break
    elif(a.lower()=="right"):
        print("Oh no! The Glitch’s trap was here! Try again. 😨")
        break
    else:
        a=input("Invalid choice. Please enter 'left' or 'right' : ")