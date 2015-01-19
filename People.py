__author__ = 'Victoria'

import sqlite3


class PeopleTable(object):
    db_name = "yellowpagersdb"

    def __init__(self, db):
        self.db_name = db

    def insert_people(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_fname = raw_input("Input first name: ")
        user_in_lname = raw_input("Input last name: ")
        user_in_abcode = raw_input("And input addressbook_code please: ")
        conn.execute("insert into people(unique_id, fname, lname, addressbook_code) values (?, ?, ?, ?)",
                     (user_in_id, user_in_fname, user_in_lname, user_in_abcode))

    def print_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute("select unique_id, fname, lname, addressbook_code from people")

        for row in cur:
            print "unique_id = ", row[0]
            print "fname = ", row[1]
            print "lname = ", row[2]
            print "addressbook_code = ", row[3], "\n"

        print "Total number of rows deleted: ", conn.total_changes

    def delete_people(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        # user_in_id = raw_input("Input unique_id: ")
        conn.execute("delete from people where unique_id = 9")