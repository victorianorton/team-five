__author__ = 'Victoria'

import sqlite3


class EmailTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_email(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_pri = raw_input("Input first email: ")
        user_in_sec = raw_input("Input second email: ")
        user_in_tri = raw_input("Input third email:: ")
        conn.execute('insert into email(unique_id, primary_email, secondary_email, third_email) values (?,?,?,?)',
                     (user_in_id, user_in_pri, user_in_sec, user_in_tri))
        conn.commit()

    def delete_email(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_pri = raw_input("Input primary email: ")
        conn.execute('delete from email where unique_id = ? and primary_email = ?', (user_in_id, user_in_pri))
        conn.commit()

    def print_email_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select unique_id, primary_email, secondary_email, third_email from email')
        conn.commit()

        for row in cur:
            print "unique_id = ", row[0]
            print "primary_email = ", row[1]
            print "secondary_mail = ", row[2]
            print "third_email = ", row[3], "\n"

        print "Total number of rows changed: ", conn.total_changes