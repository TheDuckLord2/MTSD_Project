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
		def __init__(cartID, itemID, cartTotal):
			self.cartID = cartID
			self.itemID = itemID
			self.cartTotal = 0
