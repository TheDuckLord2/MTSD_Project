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
