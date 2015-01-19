__author__ = 'Victoria'

import sqlite3


class MasterTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_master(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_abname = raw_input("Input address book name: ")
        user_in_abcode = raw_input("Input address book code: ")
        user_in_added = raw_input("Input date address book added: ")
        user_in_mod = raw_input("Input date address book last modified: ")

        conn.execute('insert into master(addressbook_name, addressbook_code, date_added, date_modified)'
                     ' values (?,?,?,?)', (user_in_abname, user_in_abcode, user_in_added, user_in_mod))
        conn.commit()

    def delete_master(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_abname = raw_input("Input address book name: ")
        conn.execute('delete from master where addressbook_name = ?', (user_in_abname,))
        conn.commit()

    def print_master_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select addressbook_name, addressbook_code, date_added, date_modified from master')
        conn.commit()

        for row in cur:
            print "address book name = ", row[0]
            print "address book code = ", row[1]
            print "date created = ", row[2]
            print "date last modified = ", row[3], "\n"

        print "Total number of rows changed: ", conn.total_changes