#!/usr/bin/python3
""" The filter based on user input
    Args:
        - username: the unsername of the mysql
        - passwd: The password for the user
        - db: database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT *
            FROM `states`
            WHERE name LIKE BINARY '{}'""".format(sys.argv[4].strip("'")))
    [print(state) for state in cur.fetchall()]
