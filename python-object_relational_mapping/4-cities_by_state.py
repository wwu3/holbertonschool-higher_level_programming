#!/usr/bin/python3
"""
Lists all cities from hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password>"
              "  <database_name>".format(sys.argv[0]))
        exit(1)

    mysql_username, mysql_password, database_name = sys.argv[1:]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            db=database_name
            )
    cur = db.cursor()
    cities_query = ("SELECT cities.id, cities.name, states.name FROM cities"
                    " INNER JOIN states ON cities.state_id = states.id;")
    cur.execute(cities_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
