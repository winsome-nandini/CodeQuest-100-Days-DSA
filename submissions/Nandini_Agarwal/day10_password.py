pswd=input("Enter your password: ")
#Taking Password input

nu=nl=nd=ns=0
#Taking variables for uppercase, lowercase, digit and special character
if len(pswd)>=8:
#Checking password is of 8 characters or not

    for ele in pswd:
    #Working with element of Password 
    
        if ele.isupper(): 
            nu=+1
        #checking is there any uppercase letter
        elif ele.islower():
            nl=+1
        #checking is there any lowercase letter
        elif ele.isdigit():
            nd=+1
        #checking is there any digit
        else:
            ns=+1
        #checking is there any special character

    if nu==nl==nd==0:
        print("Weak Password (Missing uppercase letter, lowercase letter and digits)")
    elif ns==nl==nd==0:
        print("Weak Password (Missing special characters, lowercase letter and digits)")
    elif nu==ns==nd==0:
        print("Weak Password (Missing uppercase letter, special characters and digits)")
    elif nu==nl==ns==0:
        print("Weak Password (Missing uppercase letter, lowercase letter and special characters )")

    elif nu==nl==0:
        print("Weak Password (Missing uppercase letter and lowercase letter)")
    elif ns==nl==0:
        print("Weak Password (Missing special characters and lowercase letter)")
    elif nl==nd==0:
        print("Weak Password (Missing lowercase letter and digit)")
    elif nu==ns==0:
        print("Weak Password (Missing uppercase letter and special character)")
    elif nu==nd==0:
        print("Weak Password (Missing uppercase letter and digit)")
    elif ns==nd==0:
        print("Weak Password (Missing special character and digit)")

    elif nu==0:
        print("Weak Password (Missing uppercase letter)")
    elif nl==0:
        print("Weak Password (Missing lowercase letter)")
    elif nd==0:
        print("Weak Password (Missing digit)")
    elif ns==0:
        print("Weak Password (Missing special character)")
    else:
        print("Strong Password ")

else:
    print("Weak Password (Password should have atleast 8 characters)")