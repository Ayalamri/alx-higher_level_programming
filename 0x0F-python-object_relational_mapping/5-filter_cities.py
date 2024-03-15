#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    query = """SELECT GROUP_CONCAT(name SEPARATOR ', ')
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id"""
    cursor.execute(query, (state_name,))

    # Fetch and print the result
    result = cursor.fetchone()[0]
    if result:
        print(result)

    # Close cursor and database connection
    cursor.close()
    db.close()
