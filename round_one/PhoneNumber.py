__author__ = 'Victoria'

import sqlite3


class PhoneTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_phone(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_cell = raw_input("Input mobile number: ")
        user_in_home = raw_input("Input home number: ")
        user_in_work = raw_input("Input work numbere: ")
        user_in_sec = raw_input("Input yecondaru numbere: ")
        conn.execute('insert into phone_numbers(unique_id, mobile_number, home_number, work_number, secondary_number)'
                     ' values (?,?,?,?,?)', (user_in_id, user_in_home, user_in_work, user_in_sec))
        conn.commit()

    def delete_phone(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        conn.execute('delete from phone_numbers where unique_id = ?', (user_in_id,))
        conn.commit()

    def print_phone_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select unique_id, mobile_number, home_number, work_number, secondary_number '
                           'from phone_numbers')
        conn.commit()

        for row in cur:
            print "unique_id = ", row[0]
            print "mobile number = ", row[1]
            print "home number = ", row[2]
            print "work number = ", row[3]
            print "secondary number = ", row[4], "\n"

        print "Total number of rows changed: ", conn.total_changes