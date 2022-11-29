
class User:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.userName = ""
        self.email = ""
        self.shipping = {
            "address": "",
            "city": "",
            "state": "",
            "zip": 0
        }
        self.userID = 1
        self.orderHistory = []
        self.payment = {
            "number": 0,
            "code": 0,
            "date": "",
            "address": "",
            "owner": ""
        }

    def editName(self, first, last):
        self.firstName = first
        self.lastName = last

    def editUserName(self, userName):
        self.userName = userName

    def editEmail(self, email):
        self.email = email

    def editAddress(self, address, city, state, zip):
        self.shipping = {
            "address": address,
            "city": city,
            "state": state,
            "zip": zip
        }

    def genUserID(self):
        return

    def __del__(self):
        return

    def logout(self):
        return

    def getName(self):
        return self.firstName, self.lastName

    def getEmail(self):
        return self.email

    def getShipping(self):
        return self.shipping

    def getUserID(self):
        return self.userID

    def editPayment(self, number, code, date, address, owner):
        self.payment = {
            "number": number,
            "code": code,
            "date": date,
            "address": address,
            "owner": owner
        }
