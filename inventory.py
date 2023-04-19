import sqlite3

conn = sqlite3.connect('MTSD_Database.db')

c = conn.cursor()

class inventory
    
    itemID
    itemName
    itemQuantity
    itemPrice

    def inventory():
    
    def removeItem(ItemID, Quantity):
        c.execute("UPDATE Inventory SET Quantity=? WHERE ItemID =?",(Quantity, ItemID)
        conn.commit()
