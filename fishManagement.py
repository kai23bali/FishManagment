import Inventory
import Order
import Item
import mysql.connector
import sys

# Return a connection to database
def connectDB(_database="", _host="localhost",_user="root",_password=""):
    try:
        db = mysql.connector.connect(
            host=_host,
            user=_user,
            password=_password,
            database=_database
        )
    except mysql.connector.Error as e:
        print(e)
        sys.exit()
    return db

# Close connection to database
def closeDB(db, cursor):
    cursor.close()
    db.close()

# Main Function
def main():
    # Make connection to database
    db = connectDB("fish_store")
    cursor = db.cursor()
    
    # Close connection to database
    closeDB(db, cursor)
main()
