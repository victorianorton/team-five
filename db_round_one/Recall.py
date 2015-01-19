__author__ = 'Victoria'

import sqlite3


class RecallTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_recall(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_fname = raw_input("Input first name: ")
        user_in_lname = raw_input("Input last name: ")
        conn.execute('insert into recall(fname, lname) values (?,?)',
                     (user_in_fname, user_in_lname))
        conn.commit()

    def delete_recall(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_fname = raw_input("Input first name: ")
        conn.execute('delete from recall where fname = ?', (user_in_fname,))
        conn.commit()

    def print_recall_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select fname, lname, date_searched from recall')
        conn.commit()

        for row in cur:
            print "first name = ", row[0]
            print "last name = ", row[1]
            print "date recalled = ", row[2], "\n"

        print "Total number of rows changed: ", conn.total_changes