#import mysql.connector
import sqlite3

#mydb = mysql.connector.connect(
	#cartID = "Cart ID",
	#itemID = "Item ID",
	#itemName = "Item Name",
	#itemQuantity = "Item Quantity",
	#itemPrice = "Item Price"
)
class cart:
	
	conn = sqlite3.connect('MTSD_Database.db')
	cursor = conn.cursor()
	
	
	cartID = None
	itemID = None
	cartTotal = None
	def __init__():
		cartID = mydb.cartID
		itemID = mydb.itemID
		cartTotal = 0
	def addItem(amt):
		#connect to database 
		whichItem = input("Enter the item name: ")
		howMuch = amt;
		newCartID = new_cartID()
		
		currQuantity = cursor.execute("SELECT Item Quantity FROM Inventory WHERE Item Name = ?",(whichItem))
		while howMuch > currQuantity
			howMuch = input("There are not that many items in stock. Try again. Quantity: ")
			currQuantity = cursor.execute("SELECT Item Quantity FROM Inventory WHERE Item Name = ?",(whichItem))
			
		cursor.execute("SELECT * FROM Inventory WHERE Item Name = ?",(whichItem))
		for i in range(howMuch)
			cursor.execute("INSERT INTO Cart SELECT * FROM Inventory WHERE Item Name = ? AND INSERT INTO Cart VALUES ?", (whichItem, newCartID))

		#connect to database
		#remove selected item from cart table based on specific amount
				       
	def checkout():
		#display total -> function?
		
		whichCart = input("Enter your cartID to checkout: ")
		
		
		#send order information to orderHistory DB
		cursor.execute("INSERT INTO Order History SELECT * FROM Cart WHERE Cart ID = ?", (whichCart))
		
		#remove all items from cart
		cursor.execute("DELETE * FROM Cart WHERE Cart ID = ?",(whichCart))
		# might not need the *
				   
	def new_cartID():
   		cartID++
   		return cartID	
	
	#def addTotal():
		
	
	
	conn.commit()
	conn.close()
	
