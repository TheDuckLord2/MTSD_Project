import sqlite3
conn = sqlite3.connect('MTSD_Database.db')
cursor = conn.cursor()
class cart:

	def __init__(self):
		self.cartID = None
		self.itemID = None
		self.cartTotal = 0
		
	def addItem(id, amt):
		#connect to database 
		whichItem = id
		howMuch = int(amt)
		#newCartID = cart.new_cartID()
		
		currQuantity = cursor.execute("SELECT Item_Quantity FROM Inventory WHERE ItemID = ?",(whichItem))
		currQuantity = cursor.fetchone()
		currQuantity = ''.join(map(str,currQuantity))
		currQuantity = int(currQuantity)
		quantityDiff = currQuantity - howMuch
		while howMuch > currQuantity:
			howMuch = input("There are not that many items in stock. Try again. Quantity: ")
			currQuantity = conn.execute("SELECT Item_Quantity FROM Inventory WHERE ItemID = ?",(whichItem))
			quantityDiff = currQuantity - howMuch
		#conn.execute("SELECT * FROM Inventory WHERE ItemID = ?",(whichItem))
		conn.execute("INSERT INTO Cart (ItemID,Item_Name,Item_Price,Item_Quantity) SELECT ItemID, Item_Name, Item_Price, ? FROM Inventory WHERE ItemID = ?", (howMuch, whichItem))
		conn.execute("UPDATE Cart SET Item_Quantity = ? WHERE ItemID = ?",(howMuch, whichItem))
# HAHA IT WORKS
# BUT HOW DO WE KNOW WHICH CART IS FOR WHICH USER?????????
	#	cart.addTotal(whichItem)
		cart.getTotal()

		conn.execute("UPDATE Inventory SET Item_Quantity = ? WHERE ItemID = ?",(quantityDiff,whichItem))
		conn.commit()

	def checkout():
		#display total -> function?
		cart.getTotal()
		
		whichCart = input("Enter your cartID to checkout: ")
		
		print("Order total: $" + cart.cartTotal)
		#send order information to orderHistory DB
		cursor.execute("INSERT INTO Order History SELECT * FROM Cart WHERE Cart ID = ?", (whichCart))
		
		#remove all items from cart
		cursor.execute("DELETE * FROM Cart WHERE Cart ID = ?",(whichCart))
		# might not need the *



	def getTotal():
		priceTotal = cursor.execute("SELECT SUM(Item_Price) FROM Cart")
		priceTotal = cursor.fetchone()
		return priceTotal
	
	# This was causing me some issues so I commented it out sorry

	#def addTotal(item):
		#price = cursor.execute("SELECT Item_Price FROM Inventory WHERE Item_Name = ?",(item))
		#price = cursor.fetchone()
	#	cartTotal += price
		
	def displayCart():
		cursor.execute("SELECT * FROM Inventory")
		#header = ["Item ID","Item Name","Item Quantity","Item Price"]
		# Needs to be done
	
	def new_cartID():
		cartID += 1

	#conn.commit()
	#conn.close()
	
