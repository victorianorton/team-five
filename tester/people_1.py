__author__ = 'Victoria'

import sqlite3


class PeopleTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_people(self, f, l):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('insert into people( fname, lname) values (?,?)', (f, l))
        conn.commit()
        uid = 0
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

    # def print_result(self):
    #     with sqlite3.connect(self.db_name) as conn:
    #         conn.cursor()
    #     cur = conn.execute('select unique_id, fname, lname, addressbook_code from people')
    #     conn.commit()
    #
    #     for row in cur:
    #         print "unique_id = ", row[0]
    #         print "fname = ", row[1]
    #         print "lname = ", row[2]
    #         print "addressbook_code = ", row[3], "\n"
    #
    #     print "Total number of rows deleted: ", conn.total_changes