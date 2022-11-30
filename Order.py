class Order:
    def __init__(self, db, cursor):
        self.db = db
        self.cursor = cursor

    # Generate orderID
    def _genOrderID(self, userID):
        query = "SELECT MAX(orderID) FROM orders WHERE userID=%i"
        data = (userID,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()
        
        return result[0]+1 if result != None else False

    # Add an entry to user's order history
    def addEntry(self, userID, items:tuple):
        query = "INSERT INTO orders VALUES(%i, %i, %i, %s, %i, %i, %s)"
        data = (items[0], items[1], userID, items[3], items[4], items[5], items[6])
        
        self.cursor.execute(query, data)
        self.db.commit()
    
    # View an entry from user's order history
    def viewEntry(self, userID, orderID):
        query = "SELECT * FROM orders WHERE userID=%i AND orderID=%i"
        data = (userID, orderID,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()
        
        return result if result != None else False
        
    # Clear user's entire order history
    def clearHistory(self, userID):
        query = "DELETE * FROM orders WHERE userID=%i"
        data = (userID,)
        self.cursor.execute(query, data)
        self.db.commit()
    
    # View user's entire order history
    def viewHistory(self, userID):
        query = "SELECT * FROM orders WHERE userID=%i"
        data = (userID,)
        self.cursor.execute(query, data)
        results = self.cursor.fetchall()
        
        return results