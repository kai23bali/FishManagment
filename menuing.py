import Inventory
import ShoppingCart
import User
import Order


def landingPage(cursor, db):
    while True:
        print("Welcome to the Rare Fish Store!\n\n"
              "Please select an option:\n"
              "1.\tLogin\n"
              "2.\tCreate account\n"
              "3.\tExit")
        userSel = input()
        costumer = User.User()

        match userSel:
            case "1":
                if(costumer.loginUser(cursor)):
                    userID = costumer.getID()
                    shoppingCart = ShoppingCart.ShoppingCart(userID)
                    inventory = Inventory.Inventory(cursor)
                    orders = Order.Order(db, cursor, userID)
                    pageSelect(cursor, db, shoppingCart, inventory, costumer, orders)
            case "2":
                unique = False
                userName = input("Enter username:\t")

                cursor.execute("SELECT username FROM costumer WHERE username='"
                               + userName +"';")
                result = cursor.fetchall()
                if not result:
                    unique = True
                while not unique:
                    print("Username already taken, try again")
                    userName = input("Enter username:\t")
                    cursor.execute("SELECT username FROM costumer WHERE username='"
                                   + userName + "';")
                    result = cursor.fetchall()
                    if not result: unique = True


                password = input("password:\t")
                firstName = input("First name:\t")
                lastName = input("Last name:\t")
                email = input("email:\t")

                print("Payment info:")
                number = input("Card number:\t")
                code = input("Security code:\t")
                date = input("Expiration date:\t")
                address = input("Payment address:\t")
                owner = input("Cardholder name:\t")
                paymentInfo = number +"|"+ code +"|"+ date +"|"+ address +"|"+ owner
                print("Shipping info:")
                address = input("Street address:\t")
                city = input("City:\t")
                state = input("State:\t")
                zip = input("Zip code:\t")
                shippingInfo = address +"|"+ city +"|"+ state +"|"+ zip

                costumer.createUser(cursor, firstName, lastName, password,
                                    paymentInfo, shippingInfo, userName, email)
                db.commit()
                userID = costumer.getID()
                shoppingCart = ShoppingCart.ShoppingCart(userID)
                inventory = Inventory.Inventory(cursor)
                orders = Order.Order(db, cursor, userID)
                pageSelect(cursor, db, shoppingCart, inventory, costumer, orders)
            case "3":
                print("Good Bye!")
                return

            case _:
                print("Invalid input. Please try again.\n")






def pageSelect(cursor, db, shoppingCart, inventory, user, orders): # main menu
    while True:
        print("Please select a numbered option:\n"
              "1.\tInventory\n"
              "2.\tShopping Cart\n"
              "3.\tAccount Info\n"
              "4.\tLogout")

        userSel = input()

        match userSel:
            case "1":
                inventoryMenu(cursor, db, inventory, shoppingCart)
            case "2":
                cartMenu(cursor, db, shoppingCart)
            case "3":
                if not (accountMenu(cursor, db, user, orders)):
                    return
            case "4":
                return
            case _:
                print("Invalid input. Please try again.\n")


def cartMenu(cursor, db, shoppingCart): # shopping cart selections
    while True:
        print("Shopping cart options:\n"
              "1.\tView Current Cart\n"
              "2.\tRemove Item From Cart\n"
              "3.\tClear Cart\n"
              "4.\tCheck Out\n"
              "5.\tGo Back")
        userSel = input()

        match userSel:
            case "1":
                shoppingCart.viewCart(cursor)
            case "2":
                fish = input("Which fish would you like to remove from your cart?")
                quantity = int(input("How many?"))
                shoppingCart.removeItem(fish, quantity, cursor)
                db.commit()
            case "3":
                shoppingCart.clear(cursor)
                db.commit()
            case "4":
                shoppingCart.checkOut(cursor)
                db.commit()
            case "5":
                return
            case _:
                print("Invalid input. Please try again.\n")

def inventoryMenu(cursor, db, inventory, shoppingCart):
    while True:
        print("Inventory options\n"
              "1.\tView Inventory\n"
              "2.\tAdd Item To Cart\n"
              "3.\tGo Back\n")

        userSel = input()

        match userSel:
            case "1":
                fishes = inventory.getAllItems()

                print("Fish in inventory:")
                for fish in fishes:
                    print("$" + str(fish.getPrice())+"\t"+ fish.getName()+"\n\t"+ fish.getDescription(),
                          "\n\tAvailable: ", fish.getQuantity())
                print()

            case "2":
                fish = input("Which fish would you like to add to your cart?")
                quantity = int(input("How many?"))
                shoppingCart.addItem(fish, quantity, cursor)
                db.commit()
            case "3":
                return
            case _:
                print("Invalid input. Please try again.\n")

def accountMenu(cursor, db, user, orders):
    while True:
        print("Account Options:\n"
              "1.\tEdit Account\n"
              "2.\tView Order History\n"
              "3.\tDelete Account\n"
              "4.\tGo Back")

        userSel = input()

        match userSel:
            case "1":
                print("Would you like to edit:\n"
                      "1.\tPayment information\n"
                      "2.\tShipping information\n"
                      "3.\tGo Back")
                userSel = input()
                if (userSel == "1"):
                    number = input("Card number:\t")
                    code = input("Security code:\t")
                    date = input("Expiration date:\t")
                    address = input("Payment address:\t")
                    owner = input("Cardholder name:\t")

                    user.editPayment(number, code, date, address, owner, cursor)
                    db.commit()
                    print("Payment info changed!\n")

                elif(userSel == "2"):
                    address = input("Street address:\t")
                    city = input("City:\t")
                    state = input("State:\t")
                    zip = input("Zip code:\t")

                    user.editAddress(address, city, state, zip, cursor)
                    db.commit()
                    print("Shipping info changed!\n")
                elif(userSel == "3"):
                    print()
                else:
                    print("Invalid input")

            case "2":
                results = orders.viewHistory()
                if not results:
                    print("You have no previous orders\n")
                else:
                    print("\nPast orders:")
                    for r in results:
                        print(str(r[2])+" X $"+str(r[1])+"\t"+str(r[0])+"\t"+str(r[3]))
                    print()
            case "3":
                print("Are you sure you want to delete your account? (Y/n)")
                delSel = input()
                while not (delSel == "Y" or delSel == "n"):
                    print("Invalid input. Try again")
                    print("Are you sure you want to delete your account? (Y/n)")
                    delSel = input()

                if delSel == "Y":
                    user.deleteUser(cursor)
                    db.commit()
                    return False
                else:
                    print()
            case "4":
                return True
            case _:
                print("Invalid input. Please try again.\n")

