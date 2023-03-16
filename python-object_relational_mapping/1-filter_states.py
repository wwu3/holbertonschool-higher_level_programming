#!/usr/bin/python3
"""
Import MySQLdb
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    databasename = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=databasename)
    c = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE 'N%' "
            "AND BINARY name LIKE 'N%'")
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
