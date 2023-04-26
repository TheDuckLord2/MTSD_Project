import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('MTSD_Database.db')
cursor = conn.cursor()

class cart:

	def __init__(self):
		self.itemID = None
		self.cartTotal = 0
		
	def addItem(uID, id, amt):
		#connect to database 
		whichItem = id
		howMuch = int(amt)
		#newCartID = cart.new_cartID()
		currQuantity = cursor.execute("SELECT Item_Quantity FROM Inventory WHERE ItemID = ?",(whichItem,))
		currQuantity = cursor.fetchone()
		currQuantity = ''.join(map(str,currQuantity))
		currQuantity = int(currQuantity)
		quantityDiff = currQuantity - howMuch
		while howMuch > currQuantity:
			howMuch = input("There are not that many items in stock. Try again. Quantity: ")
			currQuantity = conn.execute("SELECT Item_Quantity FROM Inventory WHERE ItemID = ?",(whichItem,))
			currQuantity = cursor.fetchone()
		quantityDiff = currQuantity - howMuch
		#conn.execute("SELECT * FROM Inventory WHERE ItemID = ?",(whichItem))
		itemID = cursor.execute("SELECT ItemID FROM Inventory WHERE ItemID = ?",(whichItem,))
		itemID = cursor.fetchone()
		print(itemID)
		itemName = cursor.execute("SELECT Item_Name FROM Inventory WHERE ItemID = ?",(whichItem,))
		itemName = cursor.fetchone()
		print(itemName)
		itemPrice = cursor.execute("SELECT Item_Price FROM Inventory WHERE ItemID = ?",(whichItem,))
		itemPrice = cursor.fetchone()
		print(itemPrice)
		conn.execute("INSERT INTO Cart (User_ID, ItemID, Item_Name, Item_Quantity, Item_Price) VALUES (?, ?, ?, ?, ?)", (uID,itemID,itemName,howMuch,itemPrice))
		conn.commit()
		print("Item/s added to cart.")
# HAHA IT WORKS
# BUT HOW DO WE KNOW WHICH CART IS FOR WHICH USER?????????
	#	cart.addTotal(whichItem)
		cart.getTotal(uID)

		conn.execute("UPDATE Inventory SET Item_Quantity = ? WHERE ItemID = ?",(quantityDiff,whichItem,))
		conn.commit()

	def checkout():
		#display total -> function?
		cart.getTotal()
		
		whichCart = input("Enter your cartID to checkout: ")
		
		print("Order total: $" + cart.cartTotal)
		#send order information to orderHistory DB
		cursor.execute("INSERT INTO Order History SELECT * FROM Cart WHERE Cart ID = ?", (whichCart,))
		
		#remove all items from cart
		cursor.execute("DELETE * FROM Cart WHERE Cart ID = ?",(whichCart,))
		# might not need the *



	def getTotal(uID):
		priceTotal = cursor.execute("SELECT SUM(Item_Price) FROM Cart WHERE User_ID = ?",(uID,))
		priceTotal = cursor.fetchone()
		return priceTotal
	
	# This was causing me some issues so I commented it out sorry

	#def addTotal(item):
		#price = cursor.execute("SELECT Item_Price FROM Inventory WHERE Item_Name = ?",(item))
		#price = cursor.fetchone()
	#	cartTotal += price
		
	def displayCart(uID):
		headers = ["Cart ID","Item ID","Item Name","Item Quantity","Item Price ($)"]
		cursor.execute("SELECT * FROM Cart WHERE UserID = ?",(uID,))
		print(tabulate(cursor.fetchall(),headers=headers))

	
