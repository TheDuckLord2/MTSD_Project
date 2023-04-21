import sqlite3
from user import user
from cart import cart

class menu:
    conn = sqlite3.connect('MTSD_Database.db')

    c = conn.cursor()

    while True:
        print("Please choose an option:")
        print("1. Log In")
        print("2. Create account")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= 3:
                pass
            elif choice < 1 or choice > 3:
                print("Invalid choice. Please enter a number between 1 and 3.")
                
        if choice == 1:
            print("Log In selected.")
            user.login()

            print("Please choose an option")
            print("1. Edit Account Information")
            print("2. Shop")
            print("3. View Cart Information")
            print("4. Log out")
            logInChoice = input("Enter your choice (1-4): ")

            if logInChoice.isdigit():
                logInChoice = int(logInChoice)
                if logInChoice >= 1 and logInChoice <= 4:
                    pass
            print("Invalid choice. Please enter a number between 1 and 4.")

            if logInChoice == 1:
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
                    
                username = input("Enter your username")
                
                if editChoice == 1
                    new_name = input("Enter your updated first name: ")
                    #do the update
                    c.execute('''UPDATE Users SET firstName = ? WHERE Username = ?''', (new_name, username))
                
                elif editChoice == 2
                    new_name = input("Enter your updated last name: ")
                    #do the update
                    c.execute('''UPDATE Users SET lastName = ? WHERE Username = ?''', (new_name, username))
                
                elif editChoice == 3
                    new_phone = input("Enter your updated phone number: ")
                    #do the update
                    c.execute('''UPDATE Users SET Phone Number = ? WHERE Username = ?''', (new_name, username))    
                
                elif editChoice == 4
                    new_phone = input("Enter your updated card information: ")
                    #do the update
                    c.execute('''UPDATE Users SET Payment Info = ? WHERE Username = ?''', (new_name, username)) 
                
                elif editChoice == 5
                    new_phone = input("Enter your updated Address: ")
                    #do the update
                    c.execute('''UPDATE Users SET Address = ? WHERE Username = ?''', (new_name, username))     
                    
                elif logInChoice == 2: 
                    print("Shop selected")
                    #show the inventory here
                    #do something to have the user be able to add to cart
                    #this should also remove one item quantity from the inventory

                elif logInChoice == 3:
                    print("View Cart Information selected")
                    #do something to show the cart information

                elif logInChoice == 4:
                    print("Log Out Selected")
                    #do something that logs the user out, this should bring user back to the first set of options
        elif choice == 2:
            print("Create account selected.")
            user.createAccount();
            print("Account created.")
        elif choice == 3:
            print("Quit selected.")
            #something should be done here to close the program??
            
        
            
    conn.commit()
    conn.close()
