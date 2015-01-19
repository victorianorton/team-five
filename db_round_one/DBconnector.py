__author__ = 'Victoria'

import os
import sqlite3


class AddressBookDB(object):
    def __init__(self, db):
        self.db_name = db

    def connect(self):
        db_new = not os.path.exists(self.db_name)

        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()

        if db_new:
            print 'Need to create a schema\n'
        else:
            print 'Database already exists\n'

    def close_conn(self):
        with sqlite3.connect(self.db_name) as conn:
                conn.cursor()
        conn.close()
