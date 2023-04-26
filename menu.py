
import sqlite3
from user import user
from cart import cart
from tabulate import tabulate
import sys
import os
import subprocess


class menu:
    conn = sqlite3.connect('MTSD_Database.db')

    c = conn.cursor()


    while True:
        print("\n\tPlease choose an option:")
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
            print("\n\tLog In selected.")
            loggedIn = user.login()
            if(loggedIn == 1):
                print("\n\tPlease choose an option")
                print("1. Edit Account Information")
                print("2. Shop")
                print("3. View Cart Information")
                print("4. View Order History")
                print("5. Log out")
                logInChoice = input("Enter your choice (1-5): ")

                if logInChoice.isdigit():
                    logInChoice = int(logInChoice)
                    if logInChoice >= 1 and logInChoice <= 5:
                        pass
                    elif logInChoice < 1 or logInChoice > 5:
                        print("Invalid choice. Please enter a number between 1 and 3.")

                if logInChoice == 1:
                    print("\n\tEdit Account Information selected")
                    username = input("Enter your username for verification: ")
                    print("\n\tPlease choose an option")
                    a = True
                    while a == True:
                        print("\n1. Edit first name")
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
                                # I think something is wrong here
                            
                        if editChoice == 1:
                            new_name = input("\nEnter your updated first name: ")
                        #do the update
                            c.execute('''UPDATE Users SET First_Name = ? WHERE Username = ?''', (new_name, username))
                            print("First name has been updated.")
                        elif editChoice == 2:
                            new_name = input("\nEnter your updated last name: ")
                            #do the update
                            c.execute('''UPDATE Users SET Last_Name = ? WHERE Username = ?''', (new_name, username))
                            print("Last name has been updated.")
                        elif editChoice == 3:
                            new_phone = input("\nEnter your updated phone number: ")
                            #do the update
                            c.execute('''UPDATE Users SET Phone_Number = ? WHERE Username = ?''', (new_name, username))    
                            print("Phone number has been updated.")
                        elif editChoice == 4:
                            new_phone = input("\nEnter your updated card information: ")
                            #do the update
                            c.execute('''UPDATE Users SET Payment_Info = ? WHERE Username = ?''', (new_name, username)) 
                            print("Card information has been updated.")
                        elif editChoice == 5:
                            new_phone = input("\nEnter your updated Address: ")
                            #do the update
                            c.execute('''UPDATE Users SET Address = ? WHERE Username = ?''', (new_name, username))     
                            print("Address information has been updated.")
                        elif editChoice == 6:
                            print("\nGo Back selected")
                            a = False
                            break
                        
                elif logInChoice == 2: 
                    print("\n\tShop selected\n")
                    
                # items = print(c.fetchall())
                    headers = ["Item ID","Item Name","Item Quantity","Item Price ($)"]
                    c.execute("SELECT * FROM Inventory")
                    print(tabulate(c.fetchall(),headers=headers))
                    add = input("Would you like to add something to your cart? (y/n) ")
                    if add == "y":
                        choice = input("\nAdd to cart (enter item ID): ")
                        quantity = input("How many would you like to add to your cart? ")
                        cart.addItem(choice, quantity)
                elif logInChoice == 3:
                    print("\n\tView Cart Information selected\n")
                    cart.displayCart()
                    print("\n\tPlease choose an option")
                    print("1. Remove from cart")
                    print("2. Checkout")
                    print("3. Go back")        
                    cartChoice = input("\nSelect an option: ")
                    if cartChoice.isdigit():
                        cartChoice = int(cartChoice)
                        if cartChoice >=1 and cartChoice <=3:
                            pass
                        else:
                            print("Invalid choice. Please enter a number between 1 and 3.")
                            continue
                    if cartChoice == 1:
                        itemtodelete = input("Enter the item ID of the item you want to remove: ")
                        itemtodelete = int(itemtodelete)
                        amttodelete = input ("How much of that item would you like to remove from your cart: ")
                        amttodelete = int(amttodelete)
                        thisMany = c.execute("SELECT Item_Quantity FROM Cart WHERE ItemID = ?",(itemtodelete,))
                        thisMany = c.fetchone()     
                        thisMany = int(''.join(map(str,thisMany)))
                        #while thisMany > amttodelete:
                    #   amttodelete = input("There are not that many items in stock. Try again. Enter the number of items you want to remove: ")
                        #  c.execute("SELECT Item_Quantity FROM Cart WHERE ItemID = ?"(itemtodelete,))
                        #  thisMany = c.fetchone()
                        newQuantity = thisMany - amttodelete
                        c.execute("DELETE FROM Cart WHERE ItemID = ?",(itemtodelete,))
                        print("Item/s removed.")
                        conn.commit()
                    # REMOVE FUNCTION WORKS YES
                elif logInChoice == 4:
                    print("\nView Order History selected\n")
                elif logInChoice == 5:
                    print("\nLog Out Selected\n")
                    loggedIn = 0
                    #do something that logs the user out, this should bring user back to the first set of options
        elif choice == 2:
            print("\n\tCreate account selected.")
            user.createAccount()
            print("Account created.")
    
    #this may not be correct
        
        
        elif choice == 3:
            print("\nQuit selected.")
            #something should be done here to close the program??
            quit()
            
    conn.commit()
    conn.close()
