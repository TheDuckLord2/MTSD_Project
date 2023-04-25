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
                while True
                print("Please choose an option")
                print("1. Edit first name")
                print("2. Edit last name")
                print("3. Edit phone number")
                print("4. Edit card information")
                print("5. Edit address information")
                print("6. Go Back")
                #each option should bring the user back to Edit account information selection
                editChoice = input("Enter your choice (1-6): ")
                if editChoice.isdigit():
                    editChoice = int(editChoice)
                    if editChoice >=1 and editChoice <=6:
                        pass
                    else:
                        print("Invalid choice. Please enter a number between 1 and 6.")
                        continue
                        
                username = input("Enter your username")
                
                if editChoice == 1:
                    new_name = input("Enter your updated first name: ")
                    #do the update
                    c.execute('''UPDATE Users SET firstName = ? WHERE Username = ?''', (new_name, username))
                    print("First Name has been updated")
                elif editChoice == 2:
                    new_name = input("Enter your updated last name: ")
                    #do the update
                    c.execute('''UPDATE Users SET lastName = ? WHERE Username = ?''', (new_name, username))
                    print("Last Name has been updated")
                elif editChoice == 3:
                    new_phone = input("Enter your updated phone number: ")
                    #do the update
                    c.execute('''UPDATE Users SET Phone Number = ? WHERE Username = ?''', (new_name, username))    
                    print("Phone number has been updated")
                elif editChoice == 4:
                    new_phone = input("Enter your updated card information: ")
                    #do the update
                    c.execute('''UPDATE Users SET Payment Info = ? WHERE Username = ?''', (new_name, username)) 
                    print("Card Information has been updated")
                elif editChoice == 5:
                    new_phone = input("Enter your updated Address: ")
                    #do the update
                    c.execute('''UPDATE Users SET Address = ? WHERE Username = ?''', (new_name, username))     
                    print("Address Information has been updated")
                elif editChoice == 6:
                    print("Go Back selected")
                    break
                    
            elif logInChoice == 2: 
                print("Shop selected")
                c.execute("SELECT * FROM Inventory")
                choice = input("Which item would you like to purchase?")
                quantity = input("How many ",choice,"s would you like to purchase?")
                cart.addItem(quantity)
                #show the inventory here
                #do something to have the user be able to add to cart
                #this should also remove one item quantity from the inventory

            elif logInChoice == 3:
                print("View Cart Information selected")
                cart.displayCart()
                print("Please choose an option")
                print("1. Delete from cart")
                print("2. Checkout")
                print("3. Go back")
                
                cartChoice = ("Select an option:")
                if cartChoice.isdigit():
                    cartChoice = int(cartChoice)
                    if cartChoice >=1 and cartChoice <=3:
                        pass
                    else:
                        print("Invalid choice. Please enter a number between 1 and 3.")
                        continue
                if cartChoice == 1:
                    itemtodelete = input("Which item would you like to delete")
                    amttodelete = input ("How much of that item would you like to delete")
                    
                    c.execute("UPDATE Cart SET Item Quantity = Quantity - {amttodelete} WHERE Item Name = ?", (itemtodelete))
                #do something to show the carwt information ,,,, still not done!!!!!!!!!!!!!!!!!!!!!!!!!

            elif logInChoice == 4:
                print("Log Out Selected")
                #do something that logs the user out, this should bring user back to the first set of options
                break
        elif choice == 2:
            print("Create account selected.")
            user.createAccount()
            print("Account created.")
    
    #this may not be correct
        
        
        elif choice == 3:
            print("Quit selected.")
            #something should be done here to close the program??
            quit()
            
    conn.commit()
    conn.close()
