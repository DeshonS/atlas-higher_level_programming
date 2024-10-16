#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa that start with N"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()