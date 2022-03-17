import sqlite3
import os

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM toolbox_airline")

    return cur.fetchall()


def fetch_airline():
    full_dir = '/'.join(os.path.dirname(__file__).split('/')[:-2])
    conn = create_connection(full_dir + "/db.sqlite3")
    return select_all(conn)
