#!/usr/bin/python3
"""
Import MySQLdb
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    c = db.cursor()
    query = ("SELECT * FROM states where name='{}'"
             "AND BINARY name='{}' ORDER"
             "BY id ASC").format(state_name_searched, state_name_searched)
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
