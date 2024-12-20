#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that match an arg"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE states.name = {}".format(sys.argv[4]))
    results = cur.fetchall()
    for res in results:
        print(res)
    cur.close()
    db.close()
