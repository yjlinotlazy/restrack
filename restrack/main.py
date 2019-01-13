import json
import pickle
import sqlite3
from sqlite3 import Error as DB_Error

DB_PATH='~/.restrack/restrack_sqlite.db'
CONFIG_PATH='~/.restrack/config.json'


class ResTracker:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def load_config(self):
        raise NotImplementedError

    def load_db(self, dbpath):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


def main():
    print("Welcome to ResTrack, a resolution progress tracking tool")
    try:
        conn = sqlite3.connect(DB_PATH)
        tracker = ResTracker(conn)
        tracker.load_config(CONFIG_PATH)
        tracker()
    except DB_Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    main()