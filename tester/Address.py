__author__ = 'Victoria'

import sqlite3


class AddressTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_address(self, uid, line_one, line_two, city, state, zip,):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()

        conn.execute('insert into address(unique_id, address_line_one, address_line_two, '
                     'city, state, zip) values (?,?,?,?,?,?)',
                     (uid, line_one, line_two, city, state, zip))
        conn.commit()
        return uid

    def delete_address(self, uid):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        conn.execute('delete from address where unique_id = ?', (uid,))
        conn.commit()
        return uid


    def address_deleted(self, uid):
        print "address uid: ", uid, ", has been deleted!"
