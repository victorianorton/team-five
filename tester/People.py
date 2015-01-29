__author__ = 'xi'

import sqlite3

# db = yellowpagerdb.db

# from searching_engine import *

class PeopleTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_people(self, f, l):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        conn.execute('insert into people( fname, lname) values (?,?)', (f, l))
        cur = conn.execute('SELECT max(unique_id) from people')
        conn.commit()

        for row in cur:
            uid = row[0]
            return uid


    def delete_people(self, uid):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        r_uid = uid
        conn.execute('delete from address where unique_id = ?', (uid,))
        conn.execute('delete from phone_number where unique_id = ?', (uid,))
        conn.execute('delete from email where unique_id = ?', (uid,))
        conn.execute('delete from people where unique_id = ?', (uid,))
        conn.commit()
        return r_uid


    def people_deleted(self, uid):
        print "people uid : ", uid, ", has been deleted!"

