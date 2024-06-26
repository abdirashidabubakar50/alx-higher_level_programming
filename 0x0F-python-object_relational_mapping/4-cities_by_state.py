#!/usr/bin/python3

"""

This is a script that lists all the cities from the database hbtn_0e_4_usa

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
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC

            """
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
