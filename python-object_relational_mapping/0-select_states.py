#!/usr/bin/python3
"""
Import MySQLdb
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    databasename = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_password, db=databasename)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
