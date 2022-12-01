class Order:
    def __init__(self, db, cursor, userID):
        self.db = db
        self.cursor = cursor
        self.userID = userID

    # Check if user has an order history
    def _userExist(self, userID):
        query = "SELECT userID FROM orders WHERE userID=%s LIMIT 0,1"
        data = (self.userID,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()

        return True if result != None else False

    # Private function that generates an orderID
    def _genOrderID(self):
        # OrderID is 1 if user has no previous order history
        if self._userExist(self.userID) == False: return 1

        # Select max orderID value from the user
        query = "SELECT MAX(orderID) FROM orders WHERE userID=%s"
        data = (self.userID,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()

        return int(result[0]) + 1 if result != None else False

    # Add an entry to user's order history
    def addEntry(self, itemList: tuple, orderTime):
        for item in itemList:
            query = "INSERT INTO orders VALUES(%s, %s, %s, %s, %s, %s)"
            data = (self._genOrderID(self.userID), item.getID(), self.userID, item.getQuantity(), item.getPrice(), orderTime)
            self.cursor.execute(query, data)
            self.db.commit()

    # View an entry from user's order history
    def viewEntry(self, orderTime):
        if self._userExist(self.userID) == False: return False

        query = "SELECT * FROM orders WHERE userID=%s AND orderTime=%s"
        data = (self.userID, orderTime,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchall()

        return result if result != None else False

    # Clear user's entire order history
    def clearHistory(self):
        query = "DELETE FROM orders WHERE userID=%s"
        data = (self.userID,)
        self.cursor.execute(query, data)
        self.db.commit()

    # View user's entire order history
    def viewHistory(self):
        if self._userExist(self.userID) == False: return False

        self.cursor.execute("SELECT name, price, quantity, orderTime"
                            " FROM orders WHERE userID='"+str(self.userID)+"';")
        results = self.cursor.fetchall()
        return results