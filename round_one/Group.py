__author__ = 'Victoria'

import sqlite3


class GroupTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_group(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_grp = raw_input("Input group type: ")
        user_in_id = raw_input("Input unique_id: ")
        conn.execute('insert into group(type, unique_id) values (?,?)',
                     (user_in_grp, user_in_id))
        conn.commit()

    def delete_group(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        user_in_id = raw_input("Input unique_id: ")
        conn.execute('delete from groups where unique_id = ?', (user_in_id,))
        conn.commit()

    def print_group_result(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        cur = conn.execute('select type, unique_id from groups')
        conn.commit()

        for row in cur:
            print "type = ", row[0]
            print "unique_id = ", row[1], "\n"

        print "Total number of rows changed: ", conn.total_changes