#!/usr/bin/python3

"""
A Script that lists all states with a name starting with N(Upper N)
from the database hgn_0e_0_usa

"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                password=passwd,
                db=db_name
            )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
