import sqlite3

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
		quantityDiff = currQuantity - howMuch
		while howMuch > currQuantity:
			howMuch = input("There are not that many items in stock. Try again. Quantity: ")
			currQuantity = cursor.execute("SELECT Item Quantity FROM Inventory WHERE Item Name = ?",(whichItem))
			quantityDiff = currQuantity - howMuch
		cursor.execute("SELECT * FROM Inventory WHERE Item Name = ?",(whichItem))
		for i in range(howMuch):
			cursor.execute("INSERT INTO Cart SELECT * FROM Inventory WHERE Item Name = ? AND INSERT INTO Cart VALUES ?", (whichItem, newCartID))
			addTotal(whichItem)
		#connect to database
		if quantityDiff > 0:
			cursor.excecute("UPDATE Inventory SET Item Quantity ? WHERE Item Name = ?",(quantityDiff,whichItem))
		#remove selected item from cart table based on specific amount
		elif quantityDiff == 0:
			cursor.execute("DELETE * FROM Inventory WHERE Item Name = ?"(whichItem))
		#or if the item doesn't get deleted:remove the if and elif, just leaving the first SQL statement
	def checkout():
		#display total -> function?
		
		whichCart = input("Enter your cartID to checkout: ")
		
		print("Order total: $" + cartTotal)
		#send order information to orderHistory DB
		cursor.execute("INSERT INTO Order History SELECT * FROM Cart WHERE Cart ID = ?", (whichCart))
		
		#remove all items from cart
		cursor.execute("DELETE * FROM Cart WHERE Cart ID = ?",(whichCart))
		# might not need the *
	def addTotal(item):
		cartTotal += cursor.execute("SELECT Item Price FROM Inventory WHERE Item Name = ?",(item))
	def new_cartID():
   		cartID += 1
	conn.commit()
	conn.close()
	
