#!/usr/bin/python3
"""
script that lists all cities
from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    INNER JOIN states \
                    ON cities.state_id = states.id \
                    ORDER BY cities.id ASC;")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()
