def pageSelect(cursor, db, shoppingCart):
    while True:
        print("Please select a numbered option:\n"
              "1.\tInventory\n"
              "2.\tShopping Cart\n"
              "3.\tAccount Info\n"
              "4.\tExit Program")

        userSel = input()

        match userSel:
            case 1:
                inventoryMenu(cursor, db)
            case 2:
                cartMenu(cursor, db, shoppingCart)
            case 3:
                accountMenu(cursor, db)
            case 4:
                return
            case _:
                print("Invalid input. Please try again.\n")


def cartMenu(cursor, db, shoppingCart):
    while True:
        print("Shopping cart options:\n"
              "1.\tView Current Cart\n"
              "2.\tRemove Item From Cart\n"
              "3.\tClear Cart\n"
              "4.\tCheck Out\n"
              "5.\tGo Back")
        userSel=input()

        match userSel:
            case 1:
                shoppingCart.viewCart(cursor)
            case 2:
                fish = input("Which fish would you like to remove from your cart?")
                quantity = int(input("How many?"))
                shoppingCart.addItem(fish, quantity, cursor)
                db.commit()
            case 3:
                shoppingCart.clear(cursor)
                db.commit()
            case 4:
                shoppingCart.checkOut(cursor)
                db.commit()
            case 5:
                return
            case _:
                print("Invalid input. Please try again.\n")

def inventoryMenu(cursor, db):
    return

def accountMenu(cursor, db):
    return