class Item:
    def __init__(self, ID=None, name="", description="", quantity=None, price=None):
        self.ID = ID
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def getID(self):
        return self.ID

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def isAvailable(self):
        if self.quantity:
            return True
        else:
            return False
