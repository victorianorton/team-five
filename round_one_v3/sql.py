__author__ = 'Victoria'

import sqlite3


class AddressBookDB:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def _query(self, q="""SELECT fname, lname from master"""):
        self.cur.execute(q)
        return self.cur.fetchall()

    def search_people(self, name):
        print(name)
        self.cur.execute("select * from master where (fname like '%"+ name +"%' or lname like '%"+ name+ "%')")
        return self.cur.fetchall()

    def insert_tb(self, data):
        self.cur.execute('select max(unique_id) from master')
        uid = self.cur.fetchone()[0] + 1
        data = (uid,) + data
        self.cur.execute('insert into master values (?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        self.conn.commit()
        '''
    def insert_people(self, items):
        self.cur.execute('select max(unique_id) from master')
        uid = self.cur.fetchone()[0] + 1
        items = (uid,) + items
        self.cur.execute('insert into master values (?,?,?)', items)
        self.conn.commit()'''

    def delete_people(self, uid):
        del_ppl = (uid,)
        self.cur.execute('delete from master where unique_id = ?', del_ppl)
        self.conn.commit()

    def insert_email(self, items):
        self.cur.execute('select max(unique_id) from master')
        uid = self.cur.fetchone()[0] + 1
        # self.cur.execute('select p.unique_id, e.unique_id from people p, email e where p.unique_id = e.unique_id')
        items = (uid,) + items
        self.cur.execute('insert into master values (?,?,?)', items)
       # self.cur.execute('insert into email values (?,?)', items)
        self.conn.commit()

    def delete_email(self, uid):
        del_email = (uid,)
        self.cur.execute('delete from master where unique_id = ?', del_email)
        self.conn.commit()

    def search_email(self, name):
        print(name)
        self.cur.execute("select * from master where email like '%"+ name +"%'")
        return self.cur.fetchall()

    def update_email(self, uid, email):
        up_email = (uid,)
        # self.conn.execute('select p.fname, p.lname from people p join email e on p.unique_id = e.unique_id')

        self.conn.execute('UPDATE master SET email = ? '
                          'WHERE unique_id = ?', (email, up_email))
        self.conn.commit()

    def insert_phone(self, items):
        self.cur.execute('select max(unique_id) from people')
        uid = self.cur.fetchone()[0] + 1
        items = (uid,) + items
        self.cur.execute('insert into master values (?,?)', items)
        self.conn.commit()

    def delete_phone(self, uid):
        del_phone = (uid,)
        self.cur.execute('delete from master where unique_id = ?', del_phone)
        self.conn.commit()

    def search_phone(self, name):
            print(name)
            self.cur.execute("select * from master where phone_number like '%"+ name +"%'")
            return self.cur.fetchall()

    def insert_address(self, items):
        self.cur.execute('select max(unique_id) from people')
        uid = self.cur.fetchone()[0] + 1
        items = (uid,) + items
        self.cur.execute('insert into master values (?,?,?,?,?,?)', items)
        self.conn.commit()

    def delete_address(self, uid):
        del_address = (uid,)
        self.cur.execute('delete from master where unique_id = ?', del_address)
        self.conn.commit()

    def search_address(self, zip):
            print(zip)
            self.cur.execute("select * from master where addresses.zip  like '%"+ zip +"%'")
            return self.cur.fetchall()

    def sorting_by_zip(self):
        self.cur.execute('SELECT * FROM people p LEFT OUTER JOIN addresses a USING (unique_id)'
                         'ORDER BY a.zip, fname')
        self.conn.commit()

        self.conn.execute('SELECT * FROM people WHERE unique_id not in '
                                      '(SELECT people.unique_id FROM addresses JOIN people '
                                      'ON (people.unique_id = addresses.unique_id))'
                                      'ORDER BY people.fname')
        self.conn.commit()

    def sort_by_name(self):
        self.cur.execute("select fname, lname from people order by fname asc")
        self.conn.commit()

    def add_user_feild(self, field):
        print(field)
        self.cur.execute("alter table master add column  '%"+ field +"%'TEXT")
        self.conn.commit()

    def close(self):
        self.conn.close()


session = AddressBookDB(sqlite3.connect('addressbook_v3.db'))
