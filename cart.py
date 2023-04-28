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
		uID = int(''.join(map(str, uID)))
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
		itemData = cursor.execute("SELECT ItemID, Item_Name, Item_Price FROM Inventory WHERE ItemID = ?",(whichItem,))
		itemData = cursor.fetchone()
		print(itemData[0])
		print(itemData[1])
		print(itemData[2])
		conn.execute("INSERT INTO Cart (User_ID, ItemID, Item_Name, Item_Quantity, Item_Price) VALUES (?, ?, ?, ?, ?)", (uID,itemData[0],itemData[1],howMuch,itemData[2]))
		conn.commit()
		print("Item/s added to cart.")
# HAHA IT WORKS
# BUT HOW DO WE KNOW WHICH CART IS FOR WHICH USER?????????
	#	cart.addTotal(whichItem)
		cart.getTotal(uID)

		conn.execute("UPDATE Inventory SET Item_Quantity = ? WHERE ItemID = ?",(quantityDiff,whichItem,))
		conn.commit()

	def checkout(uID):
		#display total -> function?
		uID = int(''.join(map(str,uID)))
		total = cart.getTotal(uID)
		addr = cursor.execute("SELECT Address FROM Users WHERE UserID = ?",(uID,))
		addr = cursor.fetchone()
		addr = ''.join(map(str,addr))
		print("Order total: $" + str(total))
		conn.execute("INSERT INTO Order_History ([User ID],[Total PRIce],[Address]) VALUES (?,?,?)",(uID,total,addr))
		#send order information to orderHistory DB
		#cursor.execute("INSERT INTO Order_History SELECT * FROM Cart WHERE User ID = ?", (uID,))
		#cursor.execute("INSERT INTO Order History (User ID, Total Price, Total Quantity, Address) VALUES ('?', '?', '?', '?')",(whichcart,
		#remove all items from cart
		cursor.execute("DELETE FROM Cart WHERE [User_ID] = ?",(uID,))
		conn.commit()
		# might not need the *



	def getTotal(uID):
		priceTotal = cursor.execute("SELECT SUM(Item_Price) FROM Cart WHERE User_ID = ?",(uID,))
		priceTotal = cursor.fetchone()
		priceTotal = float(''.join(map(str,priceTotal)))
		return priceTotal
	
	# This was causing me some issues so I commented it out sorry

	#def addTotal(item):
		#price = cursor.execute("SELECT Item_Price FROM Inventory WHERE Item_Name = ?",(item))
		#price = cursor.fetchone()
	#	cartTotal += price
		
	def displayCart(uID):
		uID = int(''.join(map(str, uID)))
		headers = ["User ID","Item ID","Item Name","Item Quantity","Item Price ($)"]
		cursor.execute("SELECT * FROM Cart WHERE User_ID = ?",(uID,))
		print(tabulate(cursor.fetchall(),headers=headers))

	
