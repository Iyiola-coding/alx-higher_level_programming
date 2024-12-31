#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server using credentials from command line arguments
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute SQL query from the file
    with open("0-select_states.sql", "r") as file:
        query = file.read()

    cursor.execute(query)

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()
