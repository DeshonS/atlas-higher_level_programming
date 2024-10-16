#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that start with N"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE"
                 "'N%' OR name LIKE 'n%' ORDER BY id ASC")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()