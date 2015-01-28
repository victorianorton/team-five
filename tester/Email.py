__author__ = 'Victoria'

import sqlite3


class EmailTable(object):
    def __init__(self, db):
        self.db_name = db

    def insert_email(self,uid, e):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        conn.execute('insert into email( unique_id, email) values (?,?)',
                     ( uid, e,))
        conn.commit()
        return uid

    def delete_email(self, uid):
        with sqlite3.connect(self.db_name) as conn:
            conn.cursor()
        conn.execute('delete from email where unique_id = ? ', (uid,))
        conn.commit()
        return uid

    def email_deleted(self, uid):
        print "email uid: ", uid, "has been deleted!"
