import Item
class Inventory:
    def __init__(self, cursor):
        self.cursor = cursor

    # Check if inventory is empty
    def isEmpty(self):
        self.cursor.execute("SELECT itemID FROM inventory LIMIT 0,1")
        result = self.cursor.fetchone()
        return True if result == None else False
    
    # Check if a specific item is available
    def isAvailable(self, itemName):
        if self.isEmpty() == True: return False
        
        query = "SELECT stock FROM inventory WHERE name=%s"
        data = (itemName,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()
        return True if result[0] > 0 else False

    # Get a specific item from inventory
    def getItem(self, itemName):
        if self.isEmpty() == True: return False
        
        query = "SELECT * FROM inventory WHERE name=%s"
        data = (itemName,)
        self.cursor.execute(query, data)
        result = self.cursor.fetchone()
        
        if result == None:
            return False
        else:
            return Item.Item(result[0], result[1], result[2], result[3], result[4])

    # Get all items from inventory
    def getAllItems(self):
        if self.isEmpty() == True: return False
        
        self.cursor.execute("SELECT * FROM inventory")
        results = self.cursor.fetchall()
        
        itemList = list()
        for row in results:
            item = Item.Item(row[0], row[1], row[2], row[3], row[4])
            itemList.append(item)
        return tuple(itemList)
    