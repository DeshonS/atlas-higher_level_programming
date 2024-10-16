#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that match an arg"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port="3306", user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = {} ORDER BY id".format(search))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
