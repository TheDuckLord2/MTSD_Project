import sqlite3
from user import user
from cart import cart
from tabulate import tabulate
from secretagain import gametime
import random
import os
import getpass_ak


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
            os.system('cls')
            print("\n\tLog In selected.")
            usern = input("Username: ")
            passw = getpass_ak.getpass("Password: ")
           # passw = input("Password: ")
            loggedIn = user.login(usern, passw)
            while(loggedIn == 1):
                uID = c.execute("SELECT UserID FROM Users WHERE Username = ?",(usern,))
                uID = c.fetchone()
                
                while True:
                    print("\n\tPlease choose an option")
                    print("1. Edit Account Information")
                    print("2. Shop")
                    print("3. View Cart Information")
                    print("4. View Order History")
                    print("5. View profile")
                    print("6. Delete Profile")
                    print("7. Log Out")
                    logInChoice = input("Enter your choice (1-7): ")

                    if logInChoice.isdigit():
                        logInChoice = int(logInChoice)
                        if logInChoice >= 1 and logInChoice <= 6:
                            pass
                        elif logInChoice < 1 or logInChoice > 6:
                            print("Invalid choice. Please enter a number between 1 and 3.")

                    if logInChoice == 1:
                        os.system('cls')
                        print("\n\tEdit Account Information selected")
                        print("\n\tPlease choose an option")
                        
                        while True:
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
                                c.execute('''UPDATE Users SET First_Name = ? WHERE Username = ?''', (new_name, usern))
                                print("First name has been updated.")
                                break
                                
                            elif editChoice == 2:
                                new_name = input("\nEnter your updated last name: ")
                                #do the update
                                c.execute('''UPDATE Users SET Last_Name = ? WHERE Username = ?''', (new_name, usern))
                                print("Last name has been updated.")
                                break
                                
                            elif editChoice == 3:
                                new_phone = input("\nEnter your updated phone number: ")
                                #do the update
                                c.execute('''UPDATE Users SET Phone_Number = ? WHERE Username = ?''', (new_name, usern))    
                                print("Phone number has been updated.")
                                break
                                
                            elif editChoice == 4:
                                new_phone = input("\nEnter your updated card information: ")
                                #do the update
                                c.execute('''UPDATE Users SET Payment_Info = ? WHERE Username = ?''', (new_name, usern)) 
                                print("Card information has been updated.")
                                break
                                
                            elif editChoice == 5:
                                new_phone = input("\nEnter your updated Address: ")
                                #do the update
                                c.execute('''UPDATE Users SET Address = ? WHERE Username = ?''', (new_name, usern))     
                                print("Address information has been updated.")
                                break
                                
                            elif editChoice == 6:
                                os.system('cls')
                                print("\nGo Back selected")
                                break
                                

                    elif logInChoice == 2: 
                        os.system('cls')
                        print("\n\tShop selected\n")

                    # items = print(c.fetchall())
                        headers = ["Item ID","Item Name","Item Quantity","Item Price ($)"]
                        c.execute("SELECT * FROM Inventory")
                        print(tabulate(c.fetchall(),headers=headers))
                        add = input("Would you like to add something to your cart? (y/n) ")
                        if add == "y":
                            choice = input("\nAdd to cart (enter item ID): ")
                            quantity = input("How many would you like to add to your cart? ")
                            if quantity.isdigit():
                                quantity = int(quantity)
                                if quantity >= 1:
                                    cart.addItem(uID,choice, quantity)
                                    break
                            elif choice < 1:
                                print("Invalid choice. Please enter a number greater than 0.")
                                break
                            os.system('cls')
                            #cart.addItem(uID,choice, quantity)
                        #os.system('cls')
                        #break
                            
                    elif logInChoice == 3:
                        os.system('cls')
                        print("\n\tView Cart Information selected\n")
                        cart.displayCart(uID)
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
                            pricey = c.execute("SELECT Item_Price FROM Inventory WHERE ItemID = ?",(itemtodelete,))
                            pricey = c.fetchone()
                            pricey = float(''.join(map(str,pricey)))
                            #while thisMany > amttodelete:
                        #   amttodelete = input("There are not that many items in stock. Try again. Enter the number of items you want to remove: ")
                            #  c.execute("SELECT Item_Quantity FROM Cart WHERE ItemID = ?"(itemtodelete,))
                            #  thisMansy = c.fetchone()
                            newQuantity = thisMany - amttodelete
                            if newQuantity > 0:
                                c.execute("UPDATE Cart SET Item_Quantity = ?, Item_Price = ? WHERE ItemID = ?",(newQuantity,pricey*newQuantity, itemtodelete,))
                            elif newQuantity <= 0:
                                c.execute("DELETE FROM Cart WHERE ItemID = ?",(itemtodelete,))
                            print("Item/s removed.")
                            conn.commit()
                        # REMOVE FUNCTION WORKS YES
                            os.system('cls')
                            break
                        if cartChoice == 2:
                            print("\tCheckout Selected\n")
                            paymentInfo = input("Please enter your payment info: ")
                            cart.checkout(uID)
                            os.system('cls')
                            print("Checkout Successful.")
                            break
                            
                    elif logInChoice == 4:
                        os.system('cls')
                        print("\nView Order History selected\n")
                        headers = ["Order ID","User ID", "Total Price ($)","Address"]
                        c.execute("SELECT * FROM Order_History WHERE [User ID] = ?",(uID))
                        print(tabulate(c.fetchall(),headers=headers))
                        break
                        
                    elif logInChoice == 5:
                        os.system('cls')
                        print("\nView Profile Selected\n")
                        user.viewProfile(uID)
                        break
                        
                    elif logInChoice == 6:
                        os.system('cls')
                        print("Delete Account Selected")
                        user.deleteProfile(uID)
                        loggedIn = 0
                        break
                        
                    elif logInChoice == 7:
                        print("\nLog Out Selected\n")
                        os.system('cls')
                        loggedIn = 0
                        break
                    elif logInChoice == 202020:
                        os.system('cls')
                        print("You found it! congrass")
                        gametime.rock_paper_scissors()
                    
                        
                   
        elif choice == 2:
            os.system('cls')
            print("\n\tCreate account selected.")
            user.createAccount()
            print("Account created.")
            os.system('cls')
        
        
        elif choice == 3:
            os.system('cls')
            print("\nQuit selected.")
            conn.commit()
            conn.close()
            quit()
        
            
    conn.commit()
    conn.close()
    
