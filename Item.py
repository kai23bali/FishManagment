
class Item:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.ID = 0
        self.quantity = ""
        self.price = 0.0

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getID(self):
        return self.ID

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def isAvailable(self):
        if self.quantity:
            return True
        else:
            return False

    def display(self):
        return

