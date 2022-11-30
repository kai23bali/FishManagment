import Inventory
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
            database="test"
        )
    except mysql.connector.Error as e:
        print(e)
        sys.exit()

    # Cursor to send queries to database
    cursor = db.cursor()
         
    # Close cursor and datebase
    cursor.close()
    db.close()

main()
