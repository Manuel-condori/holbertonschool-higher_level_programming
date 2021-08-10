#!/usr/bin/python3
"""
script that takes in the name of
a state as an argument and lists
all cities of that state, using the
database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    ST_NAME = argv[4]

    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') \
                    FROM cities \
                    INNER JOIN states \
                    ON states.name = %s \
                    WHERE cities.state_id = states.id \
                    ORDER BY cities.id ASC;", (ST_NAME,))
    rows = cursor.fetchone()
    print(rows[0] if rows[0] is not None else "")
    cursor.close()
    db.close()
