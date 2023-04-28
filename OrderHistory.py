import cart
import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('MTSD_Database.db')
cursor = conn.cursor()

class OrderHistory:
    def __init__(self) -> None:
        orderID = None
        userID = None
        orderDate = None
        totalPrice = None
    def __init__(self, uID, oD, tP):
        self.userID = uID
        self.orderDate = oD
        self.totalPrice = tP
    
    def displayHistory(uID):
        uID = int(''.join(map(str, uID)))
        headers = ["Order ID","User ID","Total Price","Address"]
        cursor.execute("SELECT * FROM Order_History WHERE User_ID = ?",(uID,))
        print(tabulate(cursor.fetchall(),headers=headers))
