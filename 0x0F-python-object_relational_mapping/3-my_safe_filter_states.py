#!/usr/bin/python3
"""
script that arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    NAME = argv[4]
    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE \
                   name = %s ORDER BY id", (NAME,))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()
