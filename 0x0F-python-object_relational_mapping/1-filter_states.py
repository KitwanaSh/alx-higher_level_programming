#!/usr/bin/python3
""" To filter stated starting witht eh letter 'N'
    Using the MySQLdb connection
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in cur.fetchall():
        if state[1][0] == 'N':
            print(state)
