#!/usr/bin/python3
""" Query database based on user input from argv list """


if __name__ == "__main__":
    import MySQLdb as sql
    import sys

    conn = sql.connect(host="localhost",
                       port=3306,
                       user=sys.argv[1],
                       passwd=sys.argv[2],
                       db=sys.argv[3],
                       charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id""".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
