__author__ = 'Victoria'

import sqlite3


class AddressTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_address(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_adnum = raw_input("Input address number: ")
        user_in_adpre = raw_input("Input address prefix: ")
        user_in_adline = raw_input("Input input address liine: ")
        user_in_adpost = raw_input("Input address postifx: ")
        user_in_city = raw_input("Input address city: ")
        user_in_state = raw_input("Input state: ")
        user_in_zip = raw_input("Input zip: ")
        user_in_type = raw_input("Input type: ")
        user_in_added = raw_input("Input date added: ")
        user_in_mod = raw_input("Input date last modified: ")
        conn.execute('insert into addresses(unique_id, address_number, address_prefix, address_line, address_postfix, '
                     'city, state, zip, type, date_added, date_modified) values (?,?,?,?,?,?,?,?,?,?,?)',
                     (user_in_id, user_in_adnum, user_in_adpre, user_in_adline, user_in_adpost, user_in_city, user_in_state,
                      user_in_zip, user_in_type, user_in_added, user_in_mod))
        conn.commit()

    def delete_address(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        conn.execute('delete from addresses where unique_id = ?', (user_in_id,))
        conn.commit()

    def print_address_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select unique_id, address_number, address_prefix, address_line, address_postfix, city, '
                           'state, zip, type, date_added, date_modified from addresses')
        conn.commit()

        for row in cur:
            print "unique_id = ", row[0]
            print "address number = ", row[1]
            print "address prefix = ", row[2]
            print "address line = ", row[3]
            print "address postfix = ", row[4]
            print "city = ", row[5]
            print "state = ", row[6]
            print "zip = ", row[7]
            print "type = ", row[8]
            print "date added = ", row[9]
            print "date modified = ", row[10], "\n"

        print "Total number of rows changed: ", conn.total_changes