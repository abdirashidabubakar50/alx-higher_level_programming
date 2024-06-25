#!/usr/bin/python3

"""
This is a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches teh argument
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

    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
