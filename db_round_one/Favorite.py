__author__ = 'Victoria'

import sqlite3


class FavoriteTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_favorite(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_fname = raw_input("Input first name: ")
        user_in_lname = raw_input("Input last name: ")
        conn.execute('insert into favorites(unique_id, fname, lname, addressbook_code) values (?,?,?,?)',
                     (user_in_id, user_in_fname, user_in_lname))
        conn.commit()

    def delete_favorite(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_fname = raw_input("Input first name: ")
        conn.execute('delete from favorites where unique_id = ? and fname = ?', (user_in_id, user_in_fname))
        conn.commit()

    def print_favorite_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select unique_id, fname, lname from favorites')
        conn.commit()

        for row in cur:
            print "unique_id = ", row[0]
            print "fname = ", row[1]
            print "lname = ", row[2], "\n"

        print "Total number of rows deleted: ", conn.total_changes