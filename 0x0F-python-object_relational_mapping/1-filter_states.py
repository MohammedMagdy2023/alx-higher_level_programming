#!/usr/bin/python3
""" select all values starts with N """


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
                WHERE name LIKE BINARY 'N%'
                ORDER BY states.id""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
