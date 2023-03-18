#!/usr/bin/python3
"""
Takes in the name of a state as an argument
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

cur = db.cursor()
cities_query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
cur.execute(cities_query, [state_name])
rows = cur.fetchall()
for row in rows:
    print(row[0], end=' ')
cur.close()
db.close()
