#!/usr/bin/python3
""" Select states of the Mysql database in ascending order"""


if __name__ == "__main__":
    import MySQLdb as sql
    import sys
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    conn = sql.connect(host="localhost",
                       port=3306,
                       user=USERNAME,
                       passwd=PASSWORD,
                       db=DATABASE,
                       charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
