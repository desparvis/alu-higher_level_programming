#!/usr/bin/python3
'''database and python
'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, db=sys.argv[3],
                         user=sys.argv[1], passwd=sys.argv[2])
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    for row in c.fetchall():
        print(row)
