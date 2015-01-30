__author__ = 'Victoria'

import sqlite3


class AddressBookDB:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def _query(self, q="""SELECT fname, lname from people"""):
        self.cur.execute(q)
        return self.cur.fetchall()

    def search_people(self, name):
        print(name)
        self.cur.execute("select * from people where (fname like '%"+ name +"%' or lname like '%"+ name+ "%')")
        return self.cur.fetchall()

    def insert_people(self, items):
        self.cur.execute('select max(unique_id) from people')
        uid = self.cur.fetchone()[0] + 1
        items = (uid,) + items
        self.cur.execute('insert into people values (?,?,?)', items)
        self.conn.commit()

    def delete_people(self, uid):
        del_ppl = (uid,)
        self.cur.execute('delete from people where unique_id = ?', del_ppl)
        self.conn.commit()

    def insert_email(self, items):
        self.cur.execute('select max(unique_id) from people')
        uid = self.cur.fetchone()[0] + 1
        # self.cur.execute('select p.unique_id, e.unique_id from people p, email e where p.unique_id = e.unique_id')
        items = (uid,) + items
        self.cur.execute('insert into email values (?,?,?)', items)
       # self.cur.execute('insert into email values (?,?)', items)
        self.conn.commit()

    def delete_email(self, uid):
        del_email = (uid,)
        self.cur.execute('delete from email where unique_id = ?', del_email)
        self.conn.commit()

    def search_email(self, name):
            print(name)
            self.cur.execute("select * from email where email like '%"+ name +"%'")
            return self.cur.fetchall()

    def insert_phone(self, items):
        self.cur.execute('select max(unique_id) from people')
        uid = self.cur.fetchone()[0] + 1
        items = (uid,) + items
        self.cur.execute('insert into phone_numbers values (?,?,?)', items)
        self.conn.commit()

    def delete_phone(self, uid):
        del_phone = (uid,)
        self.cur.execute('delete from phone_numbers where unique_id = ?', del_phone)
        self.conn.commit()

    def search_phone(self, name):
            print(name)
            self.cur.execute("select * from phone_numbers where phone_number like '%"+ name +"%'")
            return self.cur.fetchall()

    def insert_address(self, items):
        self.cur.execute('select max(unique_id) from people')
        uid = self.cur.fetchone()[0] + 1
        items = (uid,) + items
        self.cur.execute('insert into addresses values (?,?,?,?,?,?,?)', items)
        self.conn.commit()

    def delete_address(self, uid):
        del_address = (uid,)
        self.cur.execute('delete from addresses where unique_id = ?', del_address)
        self.conn.commit()

    def search_address(self, zip):
            print(zip)
            self.cur.execute("select * from addresses where addresses.zip  like '%"+ zip +"%'")
            return self.cur.fetchall()

    def sorting_by_zip(self):
        self.cur.execute('SELECT * '
                                   'FROM people p LEFT OUTER JOIN addresses a USING (unique_id)'
                                   'WHERE a.primary_add = 1 '
                                   'ORDER BY a.zip, fname')
        self.conn.commit()

        self.conn.execute('SELECT * FROM people WHERE unique_id not in '
                                      '(SELECT people.unique_id FROM addresses JOIN people '
                                      'ON (people.unique_id = addresses.unique_id))'
                                      'ORDER BY people.fname')
        self.conn.commit()

    def sort_by_name(self):
        self.cur.execute('select fname, lname from people order by fname asc')
        self.conn.commit()


    def search_name_email(self):
        self.cur.execute('select p.unique_id, p.fname, p.lname, e.email, e.label '
                         'from people p join email e using (unique_id)')
        self.conn.commit()

    def search_name_address(self):
        self.cur.execute('select p.unique_id, p.fname, p.lname, a.address_line_one, '
                         'a.address_line_two, a.city, a.state, a.zip, a.label '
                         'from people p join addresses a using (unique_id)')
        self.conn.commit()

    def search_name_phone(self):
        self.cur.execute('select p.unique_id, p.fname, p.lname, pn.phone_number, pn.label '
                         'from people p join phone_numbers using (unique_id)')
        self.conn.commit()






    def close(self):
        self.conn.close()


session = AddressBookDB(sqlite3.connect('addressbook_v2.db'))
