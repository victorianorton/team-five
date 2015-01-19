__author__ = 'Victoria'

import sqlite3


class NoteTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_note(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        user_in_added = raw_input("Input date created: ")
        user_in_mod = raw_input("Input date last modified: ")
        user_in_note = raw_input("Input note please: ")
        conn.execute('insert into personal_notes(unique_id, date_added, date_modified, note) values (?,?,?,?)',
                     (user_in_id, user_in_added, user_in_mod, user_in_note))
        conn.commit()

    def delete_note(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        conn.execute('delete from personal_notes where unique_id = ?', (user_in_id,))
        conn.commit()

    def print_note_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select unique_id, date_added, date_modified, note from personal_notes')
        conn.commit()

        for row in cur:
            print "unique_id = ", row[0]
            print "daate created = ", row[1]
            print "date modified = ", row[2]
            print "note = ", row[3], "\n"

        print "Total number of rows deleted: ", conn.total_changes