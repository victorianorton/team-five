__author__ = 'Victoria'

import sqlite3


class SearchTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_search(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_fname = raw_input("Input first name: ")
        user_in_lname = raw_input("Input last name: ")
        conn.execute('insert into search(fname, lname) values (?,?)',
                     (user_in_fname, user_in_lname))
        conn.commit()

    def delete_search(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_fname = raw_input("Input first name: ")
        conn.execute('delete from search where fname = ?', (user_in_fname,))
        conn.commit()

    def print_search_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select fname, lname, date_searched from search')
        conn.commit()

        for row in cur:
            print "first name = ", row[0]
            print "last name = ", row[1]
            print "date searched = ", row[2], "\n"

        print "Total number of rows changed: ", conn.total_changes