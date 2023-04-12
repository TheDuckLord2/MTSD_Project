while True:
    print("Please choose an option:")
    print("1. Log In")
    print("2. Create account")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")

    if choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= 3:
            break
    print("Invalid choice. Please enter a number between 1 and 3.")


if choice == 1:
    print("Log In selected.")
    print("Please choose an option")
    print("1. Edit account information")
    print("2. Shop")
    print("3. View Cart Information")
    print("4. Log out")
    logInChoice = input("Enter your choice (1-4): ")
          
    if logInChoice.isdigit():
        logInChoice = int(logInChoice)
        if logInChoice >= 1 and logInChoice <= 4:
            break
    print("Invalid choice. Please enter a number between 1 and 4.")
          
elif choice == 2:
    print("Create account selected.")
    firstName = ("Enter your first name: )
    lastName = ("Enter your last name: )
    phoneNum = ("Enter your phone number: )
    cardInfo = ("Enter your card information: )
    addy = ("Enter your address: )
    
elif choice == 3:
    print("Quit selected.")

