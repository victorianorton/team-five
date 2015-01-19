__author__ = 'Victoria'

import os
import sqlite3


class AddressBookDB(object):
    db_name = "yellowpagersdb"

    def __init__(self, db):
        self.db_name = db

    def connect(self):
        db_new = not os.path.exists(self.db_name)

        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()

        if db_new:
            return 'Need to create a schema'
        else:
            return 'Database already exists'

    def close_conn(self):
        with sqlite3.connect(self.db_name) as conn:
                conn.cursor()
        conn.commit()
        conn.close()
