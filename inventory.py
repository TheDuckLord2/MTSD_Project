import sqlite3

conn = sqlite3.connect('MTSD_Database.db')

c = conn.cursor()

class inventory:
    def __init__(self):
        self.itemID = None
        self.itemName = None 
        self.itemQuantity = None
        self.itemPrice = None

    def removeItem(ItemID, Quantity):
        c.execute("UPDATE Inventory SET Quantity=? WHERE ItemID =?",(Quantity, ItemID))
        conn.commit()
