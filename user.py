import sqlite3
import hashlib
import sys
import os
import subprocess

conn = sqlite3.connect('MTSD_Database.db')
#c = conn.execute("SELECT * FROM Users ")
c = conn.cursor()


class user:
# CREATE ACCOUNT
    def createAccount():
   # user.userID += 1
        firstName = input("Enter your first name: ")
        # setFirstName(self, firstName)
        lastName = input("Enter your last name: ")
        # setLastName(self, lastName)
        phoneNumber = input("Enter your phone number: ")
        #  setPhoneNumber(self, phoneNumber)
        paymentInfo = input("Enter your payment information: ")
        #  setPaymentInfo(self, paymentInfo)
        address = input("Enter your address: ")
        #  setAddress(self, address)
        username = input("Enter a username: ")
        #  setUsername(self, username)
        password = input("Enter a password: ")
        #  setPassword(self,password)
        # num = cursor.execute("SELECT COUNT(*) FROM Users")
        #  userID = userID + num
        #  setUserID(self,userID)

        conn.execute("INSERT INTO Users (First_Name, Last_Name, Username, Password, Address, Phone_Number, Payment_Info) VALUES (?, ?, ?, ?, ?, ?, ?)",(firstName,lastName,username,password,address,phoneNumber,paymentInfo))
        conn.commit()
        #newCartName = "Cart",user.

      #  userID = userID + 1

# LOG IN FUNCTION
    def login(usern, passw):
      
      checking = c.execute("SELECT Username, Password FROM Users WHERE Username = ? AND Password = ? AND EXISTS (SELECT Username, Password FROM Users WHERE Username = ? AND Password = ?)",(usern, passw, usern,passw))
      checking = c.fetchone()
   #   print(checking)
   #   print(checking[0], checking[1])
      if checking == None:
        print("\nWrong username or password.")
      elif usern == checking[0] and passw == checking[1]:
        print("Login successful!")
        return 1
      else:
        print("\nWrong username or password.")
        return 0
       # subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        #maybe go back to original create account screen from there?

    def deleteProfile(uID):
        uID = int(''.join(map(str,uID)))
        conf = input("Are you sure you want to delete your account?(y,n)")
        if conf == 'y':
          conf = input("Are you sure you're sure you want to delete your account?(y,n)")
          if conf == 'y':
            conf = input("Are you sure you're sure you're sure you want to delete your account?(y,n)")
            if conf == 'y':
              conf = input("like, 100%, sure??(y,n)")
              if conf == 'y':
                print("Truly a travesty, but nonetheless, enjoy the rest of your day. Goodbye. :'^(")
                c.execute("DELETE FROM Users where UserID = ?",(uID,))
                return
        print("Oh, thank goodness. I got worried there.")

    def viewProfile(uID):
        uID = int(''.join(map(str, uID)))
        userData = c.execute("SELECT * FROM Users WHERE UserID = ?",(uID,))
        userData = c.fetchone()
        print("Username: " + userData[2])
        print("Full Name: " + userData[0] + " " + userData[1])
        print("Address: " + userData[5])
        print("Phone Number: " + userData[6])
        print("Payment Info: " + userData[7])
   
