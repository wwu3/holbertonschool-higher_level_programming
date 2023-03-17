#!/usr/bin/python3
"""
Prevention from MySQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: {} mysql_username mysql_password database_name"
          " state_name_searched".format(sys.argv[0]))
        exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, [state_name_searched])
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


