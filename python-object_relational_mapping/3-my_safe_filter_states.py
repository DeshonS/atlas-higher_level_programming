#!/usr/bin/python3
"""displays all values in state that meet arg"""

import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = {} ORDER BY id ASC".format(search))
        result = cur.fetchall()
        for res in result:
            print(res)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error {}".format(e))
        sys.exit(1)
    