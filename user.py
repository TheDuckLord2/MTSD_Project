import sqlite3
import hashlib


conn = sqlite3.connect('MTSD_Database.db')

c = conn.cursor()


class user:

# on log in: use cursor.execute("SELECT from where username = and password = ")

    

  # Default constructor - probably won't need it
<<<<<<< Updated upstream
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
    


    # INCREMENTS EACH NEW USERID EACH TIME THE FUNCTION IS CALLED
   # userID = 1
   # def new_userID():
    #    newUserID = userID + 1
     #   return newUserID



  # Overloaded constructor - probably won't need it either
    #def __init__(self,fn,ln,em,pn,pi,ad,usn,psw,usID):
      #  self.firstName = fn
     #   self.lastName = ln
     #   self.email = em
     #   self.phoneNumber = pn
     #   self.paymentInfo = pi
     #   self.address = ad
      #  self.username = usn
       # self.password = psw
       # self.userID = usID


  # CREATE ACCOUNT
    userID = 1;
    def createAccount():
        firstName = input("Enter your first name: ")
       # setFirstName(self, firstName)
        lastName = input("Enter your last name: ")
       # setLastName(self, lastName)
        email = input("Enter your email: ")
      #  setEmail(self, email)
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
  
        c.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (firstName,lastName,email,phoneNumber,paymentInfo,address,username,password))
  # LOG IN FUNCTION
    def login():
        user = input("Username: ")
        passw = input("Password: ")
    
        checkingUser = c.execute("SELECT Username FROM Users WHERE Username=?",(user,))
        checkingPass = c.execute("SELECT Password FROM Users WHERE Password=?",(passw,))
        if user == checkingUser and passw == checkingPass:
          print("Login successful!")
        else:
          print("Wrong username or password.")
        #  continue
          #maybe go back to original create account screen from there?
  
  
    #def logout():
    # do not know what will be here
  

    def viewProfile():
        print("Name: ", user.firstName," ",user.lastName)
        print("User ID: ", user.userID)
        print("Username: ",user.username)
        print("Email: ",user.email)
        print("Phone Number: ",user.phoneNumber)
        print("Address: " + user.address)
        print("Payment Information: ",user.paymentInfo)
    
    def setFirstName(self,x):
        self._firstName = x
    def getFirstName(self):
        return self._firstName
    def setLastName(self,x):
        self._lastName = x
    def getLastName(self):
        return self._lastName
    def setEmail(self,x):
        self._email = x
    def getEmail(self):
        return self._email
    def setPhoneNumber(self,x):
        self._phoneNumber = x
    def getPhoneNumber(self):
        return self._phoneNumber
    def setAddress(self,x):
        self._address = x
    def getAddress(self):
        return self._address
    def setPaymentInfo(self,x):
        self._paymentInfo = x
    def getPaymentInfo(self):
        return self._paymentInfo
    def setUsername(self, x):
        self._username = x
    def getUsername(self):
        return self._username
    def setPassword(self,x):
        self._password = x
    def getPassword(self):
        return self._password
    def setUserID(self,x):
        self._userID = x
    def getUserID(self):
        return self._userID
=======
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
  


  # INCREMENTS EACH NEW USERID EACH TIME THE FUNCTION IS CALLED
  # userID = 1
  # def new_userID():
  #    newUserID = userID + 1
    #   return newUserID



# Overloaded constructor - probably won't need it either
  #def __init__(self,fn,ln,em,pn,pi,ad,usn,psw,usID):
    #  self.firstName = fn
    #   self.lastName = ln
    #   self.email = em
    #   self.phoneNumber = pn
    #   self.paymentInfo = pi
    #   self.address = ad
    #  self.username = usn
      # self.password = psw
      # self.userID = usID


# CREATE ACCOUNT
  userID = 1;
  def createAccount():
    firstName = input("Enter your first name: ")
      # setFirstName(self, firstName)
    lastName = input("Enter your last name: ")
      # setLastName(self, lastName)
    email = input("Enter your email: ")
    #  setEmail(self, email)
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
    c.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(firstName,lastName,email,phoneNumber,paymentInfo,address,username,password))
  conn.commit()


# LOG IN FUNCTION
  def login():
      user = input("Username: ")
      passw = input("Password: ")
  
      checkingUser = c.execute("SELECT Username FROM Users WHERE Username=?",(user,))
      checkingPass = c.execute("SELECT Password FROM Users WHERE Password=?",(passw,))
      if user == checkingUser and passw == checkingPass:
        print("Login successful!")
      else:
        print("Wrong username or password.")
      #  continue
        #maybe go back to original create account screen from there?


  #def logout():
  # do not know what will be here


  def viewProfile(self):
      print("Name: " + self.firstName + " " + self.lastName)
      print("User ID: " + self.userID)
      print("Username: " + self.username)
      print("Email: " + self.email)
      print("Phone Number: " + self.phoneNumber)
      print("Address: " + self.address)
      print("Payment Information: "+ self.paymentInfo)
  
  def setFirstName(self,x):
      self._firstName = x
  def getFirstName(self):
      return self._firstName
  def setLastName(self,x):
      self._lastName = x
  def getLastName(self):
      return self._lastName
  def setEmail(self,x):
      self._email = x
  def getEmail(self):
      return self._email
  def setPhoneNumber(self,x):
      self._phoneNumber = x
  def getPhoneNumber(self):
      return self._phoneNumber
  def setAddress(self,x):
      self._address = x
  def getAddress(self):
      return self._address
  def setPaymentInfo(self,x):
      self._paymentInfo = x
  def getPaymentInfo(self):
      return self._paymentInfo
  def setUsername(self, x):
      self._username = x
  def getUsername(self):
      return self._username
  def setPassword(self,x):
      self._password = x
  def getPassword(self):
      return self._password
  def setUserID(self,x):
      self._userID = x
  def getUserID(self):
      return self._userID

# idea for a menu class
#while 1:
#  print("Login System")
#  print("Options: /n1. Create Account /n2. Login /n3. Exit")
#  answer = int(input("Enter an option: "))
#  if answer == 1:
#    createAccount()
#  elif answer == 2:
#    login()
#  elif answer == 3:
#    break
#else:
#   break

>>>>>>> Stashed changes









