__author__ = 'Victoria'

import sqlite3

from searching_engine import *


class PhoneTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_phone(self, uid, phone):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        conn.execute('insert into phone_number( unique_id, phone_number)'
                     ' values (?,?)', (uid, phone))
        conn.commit()

    def delete_phone(self, uid):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        conn.execute('delete from phone_number where unique_id = ?', (uid,))
        conn.commit()
        return uid

    def phone_delete(self, uid):
        print "phone with uid : ", uid, "has been deleted!"
