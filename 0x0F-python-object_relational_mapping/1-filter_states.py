#!/usr/bin/python3
""" select all values starts with N """


if __name__ == "__main__":
    import MySQLdb as sql
    import sys

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    conn = sql.connect(host="localhost",
                       port=3306,
                       username=USERNAME,
                       password=PASSWORD,
                       database=DATABASE
                       charset="uft8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
