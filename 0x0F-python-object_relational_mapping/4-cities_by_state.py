#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               ORDER BY cities.id"""
    cursor.execute(query)

    # Fetch all rows and print them
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
