import time


class ShoppingCart:
    def __init__(self, userID):
        self.userID = userID

    def viewCart(self, cursor):
        cursor.execute("SELECT itemID, quantity FROM shoppingcart WHERE userID=" + str(self.userID) + ";")
        results = cursor.fetchall()

        totalCost = 0.0

        if not results:
            print("Shopping cart is empty\n")
            return

        for items in results:
            cursor.execute("SELECT name, price FROM inventory WHERE itemID=" + str(items[0]) + ";")
            itemInfo = cursor.fetchall()
            print(itemInfo[0][0], "\t$", itemInfo[0][1], "\tX ", items[1])
            totalCost += float(itemInfo[0][1]) * float(items[1])
        print("\nCart Cost: $", "%.2f" % totalCost, "\n")

    def addItem(self, item, quantity, cursor):  # requires connection.commit() following function call
        if quantity < 1:
            print("Invalid quantity\n")
            return
        cursor.execute("SELECT itemID, stock FROM inventory WHERE name='" + item + "';")
        inventoryInfo = cursor.fetchall()

        if not inventoryInfo:
            print("Invalid fish name\n")
            return

        cursor.execute("SELECT quantity FROM shoppingcart WHERE itemID="+str(inventoryInfo[0][0])+
                       " AND userID ="+str(self.userID)+";")
        prevCartInfo = cursor.fetchall()

        addto = False #tracks whether it is adding to previous cart entry
        if prevCartInfo:
            print("&&&")
            prevQuantity = prevCartInfo[0][0]
            addto = True
        else:
            prevQuantity = 0


        if inventoryInfo[0][1] < (quantity+prevQuantity):
            print("We do not have enough of your desired fish\n")
            return

        print(quantity+prevQuantity)
        if addto:
            query = "UPDATE shoppingcart SET quantity=" + str(quantity+prevQuantity) + "" \
                    " WHERE itemID="+str(inventoryInfo[0][0])+" AND userID="+str(self.userID)+";"
            cursor.execute(query)
        else:
            query = "INSERT INTO shoppingcart (userID, itemID, quantity) VALUES (%s, %s, %s)"
            data = (self.userID, inventoryInfo[0][0], quantity)
            cursor.execute(query, data)
        print(quantity, " ", item, " successfully added to cart!\n")

    def removeItem(self, item, quantity, cursor):  # requires connection.commit() following function call
        if quantity < 1:
            print("Invalid quantity\n")
            return

        cursor.execute("SELECT itemID, quantity FROM shoppingcart WHERE userID=" + str(self.userID) +
                       " AND itemID=(SELECT itemID FROM inventory WHERE name='" + item + "');")
        result = cursor.fetchall()

        if not result:
            print("Fish name not found in cart\n")
            return

        if int(result[0][1]) < quantity:
            print("Invalid quantity\n")
            return
        elif int(result[0][1]) == quantity:
            cursor.execute("DELETE FROM shoppingcart WHERE userID=" + str(self.userID)
                           +" AND itemID = (SELECT itemID FROM inventory WHERE name='" + item + "');")
            return


        cursor.execute("UPDATE shoppingcart SET quantity=" + str(int(result[0][1]) - quantity) +
                       " WHERE userID=" + str(self.userID) +
                       " AND itemID = (SELECT itemID FROM inventory WHERE name='" + item + "');")

    def checkOut(self, cursor):  # requires connection.commit() following function call
        cursor.execute("SELECT itemID, quantity FROM shoppingcart WHERE userID=" + str(self.userID) + ";")
        results = cursor.fetchall()

        if not results:
            print("Shopping cart is empty\n")
            return

        for item in results:  # makes sure there are enough items in stock for checkout
            cursor.execute("SELECT stock, name FROM inventory WHERE itemID=" + str(item[0]))
            itemStock = cursor.fetchall()
            if itemStock[0][0] < item[1]:
                print("There are not enough " + itemStock[0][1] + " in stock. There are only " + str(item[1]) +
                      " in stock\n")
                return

        totalPrice = 0.0
        orderTime = time.asctime()
        for item in results:  # decrease stock by amount being purchased
            cursor.execute("SELECT stock, price, name FROM inventory WHERE itemID=" + str(item[0]) + ";")
            itemStock = cursor.fetchall()
            cursor.execute(
                "UPDATE inventory SET stock=" + str(int(itemStock[0][0] - int(item[1]))) + " WHERE itemID=" + str(item[
                    0]) + ";")
            query = "INSERT INTO orders (itemID, userID, name, quantity, price, orderTime)" \
                    "VALUES (%s, %s, %s, %s, %s, %s)"
            data = (item[0], self.userID, itemStock[0][2], item[1],itemStock[0][1], orderTime)
            cursor.execute(query, data)
            cursor.execute("DELETE FROM shoppingcart WHERE userID=" + str(self.userID) + " AND itemID=" + str(item[0]) + ";")
            totalPrice += float(itemStock[0][1]) * float(item[1])

        print("Checkout complete! Your total is $", "%.2f" % totalPrice, "\n")

    def clear(self, cursor):  # requires connection.commit() following function call
        cursor.execute("DELETE FROM shoppingcart WHERE userID=" + str(self.userID) + ";")
        print("Your shopping cart has been cleared\n")
