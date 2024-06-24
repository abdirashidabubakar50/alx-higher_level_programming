#!/usr/bin/python3
"""

A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usawhere name matches the argument

"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    passwrd = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                password=passwrd,
                db=db_name,
            )
    cur = db.cursor()

    query = "SELECT id, name FROM states WHERE name LIKE '{}%' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()