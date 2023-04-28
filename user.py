import sqlite3
import hashlib
import sys
import os
import subprocess

conn = sqlite3.connect('MTSD_Database.db')
#c = conn.execute("SELECT * FROM Users ")
c = conn.cursor()


class user:
    userID = 0
 # userID = 6
# on log in: use cursor.execute("SELECT from where username = and password = ")

    

  # Default constructor - probably won't need it
    def __init__(self):
      self.firstName = None
      self.lastName = None
      self.email = None
      self.phoneNumber = None
      self.paymentInfo = None
      self.address = None
      self.username = None
      self.password = None
      self.userID = None


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
            conf = input("Are you sure you're sure you want to delete your account?(y,n)")
            if conf == 'y':
              conf = input("like, 100%, sure??(y,n)")
              if conf == 'y':
                print("Okay! Enjoy the rest of your day. Goodbye.")
                c.execute("DELETE FROM Users where UserID = ?",(uID))
  #def logout():
  # do not know what will be here


    def viewProfile(uID):
        uID = int(''.join(map(str, uID)))
        userData = c.execute("SELECT * FROM Users WHERE UserID = ?",(uID,))
        userData = c.fetchone()
        print("Username: " + userData[2])
        print("Full Name: " + userData[0] + " " + userData[1])
        print("Address: " + userData[5])
        print("Phone Number: " + userData[6])
        print("Payment Info: " + userData[7])
    
    #def setFirstName(self,x):
    #  self._firstName = x
    #def getFirstName(self):
    #  return self._firstName
    #def setLastName(self,x):
    #  self._lastName = x
    #def getLastName(self):
    #  return self._lastName
    #def setEmail(self,x):
    #  self._email = x
    #def getEmail(self):
    #  return self._email
    #def setPhoneNumber(self,x):
    #  self._phoneNumber = x
    #def getPhoneNumber(self):
    #  return self._phoneNumber
    #def setAddress(self,x):
    #  self._address = x
    #def getAddress(self):
    #  return self._address
    #def setPaymentInfo(self,x):
    #  self._paymentInfo = x
    #def getPaymentInfo(self):
    #  return self._paymentInfo
    #def setUsername(self, x):
    #  self._username = x
    #def getUsername(self):
    #  return self._username
    #def setPassword(self,x):
    #  self._password = x
    #def getPassword(self):
    #  return self._password
    #def setUserID(self,x):
    #  self._userID = x
    #def getUserID(self):
    #  return self._userID
    #












