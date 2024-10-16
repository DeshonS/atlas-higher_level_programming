#!/usr/bin/python3
"""lists all cities from database"""


import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN cities.name ON cities.state_id = states.id ORDER BY cities.id")
    result = cur.fetchall()
    for res in result:
        print(res)
    cur.close()
    db.close()