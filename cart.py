import sqlite3
conn = sqlite3.connect('MTSD_Database.db')
cursor = conn.cursor()
class cart:
	
	
	def __init__(self):
		self.cartID = None
		self.itemID = None
		self.cartTotal = 0
		
	def addItem(amt):
		#connect to database 
		whichItem = input("Enter the item name: ")
		howMuch = amt;
		newCartID = cart.new_cartID()
		
		currQuantity = cursor.execute("SELECT Item Quantity FROM Inventory WHERE Item Name = ?",(whichItem))
		quantityDiff = currQuantity - howMuch
		while howMuch > currQuantity:
			howMuch = input("There are not that many items in stock. Try again. Quantity: ")
			currQuantity = cursor.execute("SELECT Item Quantity FROM Inventory WHERE Item Name = ?",(whichItem))
			quantityDiff = currQuantity - howMuch
		cursor.execute("SELECT * FROM Inventory WHERE Item Name = ?",(whichItem))
		for i in range(howMuch):
			cursor.execute("INSERT INTO Cart SELECT * FROM Inventory WHERE Item Name = ? AND INSERT INTO Cart VALUES ?", (whichItem, newCartID))
			cart.addTotal(whichItem)
		#connect to database
		cursor.excecute("UPDATE Inventory SET Item Quantity ? WHERE Item Name = ?",(quantityDiff,whichItem))
	def checkout():
		#display total -> function?
		
		whichCart = input("Enter your cartID to checkout: ")
		
		print("Order total: $" + cart.cartTotal)
		#send order information to orderHistory DB
		cursor.execute("INSERT INTO Order History SELECT * FROM Cart WHERE Cart ID = ?", (whichCart))
		
		#remove all items from cart
		cursor.execute("DELETE * FROM Cart WHERE Cart ID = ?",(whichCart))
		# might not need the *
	def addTotal(item):
		cartTotal += cursor.execute("SELECT Item Price FROM Inventory WHERE Item Name = ?",(item))
		
	def displayCart():
		cursor.execute("SELECT * FROM Inventory")
		items = cursor.fetchall()
		for item in items:
			print(item[0] + " " + item[1])
		# Needs to be done
	
	def new_cartID():cartID += 1
	conn.commit()
	conn.close()
	
