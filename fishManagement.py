import mysql.connector
import sys
import menuing

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

    # Cursor to send queries to database
    cursor = db.cursor()

    menuing.landingPage(cursor, db)

         
    # Close cursor and datebase
    cursor.close()
    db.close()

main()
