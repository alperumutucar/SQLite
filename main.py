import sqlite3
from sqlite3 import Error


def create_connection(db_file) -> object:
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

if __name__ == '__main__':
    conn = create_connection("/home/alper/PycharmProjects/SQLite/hostfiledb")

cur = conn.cursor()

cur.execute("INSERT INTO env(envApi) VALUES ('gonzales')")
conn.commit()
cur.execute("INSERT INTO partners(pName) VALUES ('piratesquad')")
conn.commit()

cur.execute("DELETE FROM env")
conn.commit()
cur.execute("DELETE FROM partners")
conn.commit()

print("success")
#cur.execute("DELETE FROM env")
#cur.execute("DELETE FROM partner")
