class menu
import sqlite3
import user
import cart
import inventory

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
    print("1. Edit Account Information")
    print("2. Shop")
    print("3. View Cart Information")
    print("4. Log out")
    logInChoice = input("Enter your choice (1-4): ")
          
    if logInChoice.isdigit():
        logInChoice = int(logInChoice)
        if logInChoice >= 1 and logInChoice <= 4:
            break
    print("Invalid choice. Please enter a number between 1 and 4.")
          
        if logInChoice == 1 
            print("Edit Account Information selected")
            print("Please choose an option")
            print("1. Edit first name")
            print("2. Edit last name")
            print("3. Edit phone number")
            print("4. Edit card information")
            print("5. Edit address information")
            #each option should bring the user back to Edit account information selection
            editChoice = input("Enter your choice (1-5): ")
            if editChoice.isdigit():
                editChoice = int(editChoice)
                if editChoice >=1 and editChoice <=5:
                    break
            print("Invalid choice. Please enter a number between 1 and 5.")
            
                if editChoice == 1
                    conn = sqlite3.connect('MTSD_Database.db')
                    c = conn.cursor()
                    
                    new_name = input("Enter your name: ")
                    #do the update
                    c.execute('''UPDATE Users SET firstName = ? WHERE id = ?''', (new_name, UserID))#NOT DONE HERE
                    
      
        elif logInChoice == 2 
            print("Shop selected")
            #show the inventory here
            #do something to have the user be able to add to cart
            #this should also remove one item quantity from the inventory
            
        elif logInChoice == 3
            print("View Cart Information selected")
            #do something to show the cart information
            
        elif logInChoice == 4
            print("Log Out Selected")
            #do something that logs the user out, this should bring user back to the first set of options
elif choice == 2:
    print("Create account selected.")
    firstName = ("Enter your first name: )
    lastName = ("Enter your last name: )
    phoneNum = ("Enter your phone number: )
    cardInfo = ("Enter your card information: )
    addy = ("Enter your address: )
    
elif choice == 3:
    print("Quit selected.")
    #something should be done here to close the program??
