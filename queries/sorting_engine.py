__author__ = 'xi'

import sqlite3
from searching_driver import *

db_name = "yellowpagersdb.db"
AddressBookDB(db_name).connect()



def sorting_by_zip():
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_address = conn.execute('SELECT * '
                               'FROM people p LEFT OUTER JOIN addresses a USING (unique_id)'
                               'WHERE a.primary_add = 1 '
                               'ORDER BY a.zip, fname')
    conn.commit()
    for row in cur_address:
        uid = row[0]
        print"-----------------------------------------------------"
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
        print_personal_notes(conn, uid)


    cur_no_address = conn.execute('SELECT * FROM people WHERE unique_id not in '
                                  '(SELECT people.unique_id FROM addresses JOIN people '
                                  'ON (people.unique_id = addresses.unique_id))'
                                  'ORDER BY people.fname')
    conn.commit()
    for row in cur_no_address:
        uid = row[0]
        print"-----------------------------------------------------"
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
        print_personal_notes(conn, uid)



sorting_by_zip()