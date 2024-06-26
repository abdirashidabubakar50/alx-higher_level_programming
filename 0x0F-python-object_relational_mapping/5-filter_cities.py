#!/usr/bin/python3

"""

This is a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                password=password,
                db=db_name
            )

    cur = db.cursor()

    query = """
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s

            """
    cur.execute(query,(state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
