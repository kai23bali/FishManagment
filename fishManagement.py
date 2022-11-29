import Inventory
import menuing
import ShoppingCart
import mysql.connector
import sys

# Main Function
def main():
    # Connect to database
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="fish management"
        )
    except mysql.connector.Error as e:
        print(e)
        sys.exit()

    SC = ShoppingCart.ShoppingCart(1)


    # Cursor to send queries to database
    cursor = db.cursor()

    menuing.pageSelect(cursor, db, SC)


         
    # Close cursor and datebase
    cursor.close()
    db.close()

main()
