import mysql.connector

mydb = mysql.connector.connect(
	cartID = "Cart ID",
	itemID = "Item ID",
	itemName = "Item Name",
	itemQuantity = "Item Quantity",
	itemPrice = "Item Price"
)
class cart:
	cartID = None
	itemID = None
	cartTotal = None
	def __init__():
		cartID = mydb.cartID
		itemID = mydb.itemID
		cartTotal = 0
	def addItem(amt):
		#connect to database
		#take selected item and add to cart table
	def removeItem(amt):
		#connect to database
		#remove selected item from cart table based on specific amount
	def checkout():
		#display total
		#send order information to orderHistory DB
		#remove all items from cart
	
