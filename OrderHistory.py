import cart
import sqlite3

conn = sqlite3.connect('MTSD_Database.db')
cursor = conn.cursor()
#commit
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
    def getOrderID(self):
        return self.orderID
    def getUserID(self):
        return self.userID
    def getOrderDate(self):
        return self.orderDate
    def getTotalPrice(self):
        return self.totalPrice
