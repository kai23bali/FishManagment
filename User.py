
class User:
    def __init__(self, ):
        self.userID = 0

    def getID(self):
        return self.userID

    def createUser(self,cursor, firstName, lastName, passcode, paymentInfo,
                   shippingAddress, userName, email):
        query = "INSERT INTO costumer" \
                "(firstName, lastName, passcode, paymentInfo," \
                "shippingAddress, userName, email)" \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);"
        values = (firstName, lastName, passcode, paymentInfo,
                   shippingAddress, userName, email)
        cursor.execute(query, values)


        cursor.execute("SELECT userID FROM costumer WHERE username='" + userName + "';")
        self.userID = cursor.fetchone()[0]

    def loginUser(self, cursor):
        username = input("Username:\t")
        password = input("Password:\t")
        cursor.execute("SELECT userID FROM costumer WHERE username='" + username+ "' AND passcode='" + password + "';")
        result = cursor.fetchall()
        if result:
            self.userID = int(result[0][0])
            print("Login successful")
            return True

        print("Incorrect username/password\n")
        return False


    def editAddress(self, address, city, state, zip, cursor):

        cursor.execute("UPDATE costumer SET shippingAddress='" +
                       (address +"|"+ city +"|"+ state +"|"+ zip)
                       + "' WHERE userID='" + str(self.userID) + "';")


    def editPayment(self, number, code, date, address, owner, cursor):

        cursor.execute("UPDATE costumer SET paymentInfo='" +
                       (number +"|"+ code +"|"+ date +"|"+ address +"|"+ owner)
                       + "' WHERE userID='" + str(self.userID) + "';")

    def deleteUser(self, cursor):
        cursor.execute("DELETE FROM orders WHERE userID="+str(self.userID)+";")
        cursor.execute("DELETE FROM shoppingcart WHERE userID="+str(self.userID)+";")
        cursor.execute("DELETE FROM costumer WHERE userID="+str(self.userID)+";")

        print("User account deleted\n")

