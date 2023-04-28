import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('MTSD_Database.db')
cursor = conn.cursor()

class cart:

	def __init__(self):
		self.itemID = None
		self.cartTotal = 0
		
	def addItem(uID, id, amt):
		whichItem = id
		uID = int(''.join(map(str, uID)))
		howMuch = int(amt)
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
		itemData = cursor.execute("SELECT ItemID, Item_Name, Item_Price FROM Inventory WHERE ItemID = ?",(whichItem,))
		itemData = cursor.fetchone()
		conn.execute("INSERT INTO Cart (User_ID, ItemID, Item_Name, Item_Quantity, Item_Price) VALUES (?, ?, ?, ?, ?)", (uID,itemData[0],itemData[1],howMuch,itemData[2]*howMuch))
		conn.commit()
		print("Item/s added to cart.")

		cart.getTotal(uID)

		conn.execute("UPDATE Inventory SET Item_Quantity = ? WHERE ItemID = ?",(quantityDiff,whichItem,))
		conn.commit()

	def checkout(uID):
		uID = int(''.join(map(str,uID)))
		total = cart.getTotal(uID)
		addr = cursor.execute("SELECT Address FROM Users WHERE UserID = ?",(uID,))
		addr = cursor.fetchone()
		addr = ''.join(map(str,addr))
		print("Order total: $" + str(total))
		conn.execute("INSERT INTO Order_History ([User ID],[Total PRIce],[Address]) VALUES (?,?,?)",(uID,total,addr))
		cursor.execute("DELETE FROM Cart WHERE [User_ID] = ?",(uID,))
		conn.commit()



	def getTotal(uID):
		priceTotal = cursor.execute("SELECT SUM(Item_Price) FROM Cart WHERE User_ID = ?",(uID,))
		priceTotal = cursor.fetchone()
		priceTotal = float(''.join(map(str,priceTotal)))
		return priceTotal
	

		
	def displayCart(uID):
		uID = int(''.join(map(str, uID)))
		headers = ["User ID","Item ID","Item Name","Item Quantity","Item Price ($)"]
		cursor.execute("SELECT * FROM Cart WHERE User_ID = ?",(uID,))
		print(tabulate(cursor.fetchall(),headers=headers))

	
