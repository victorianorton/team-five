__author__ = 'xi'

import sqlite3
from DBconnector import AddressBookDB
from searching_driver import *


db_name = "yellowpagersdb.db"

def email_editor(uid, first, second, third):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE email SET primary_email = ?, '
                 'secondary_email = ?, third = ?  WHERE unique_id = ?', (first, second, third, uid))
    conn.commit()
    print_email(conn, uid)


def address_editor(uid, number, prefix, line, postfix, city, state, zip, type):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE addresses SET address_number = ?, address_prefix = ?, address_line = ?, '
                 'address_postfix = ?, city = ?, state = ?, zip = ?, type = ? '
                 'WHERE unique_id = ?', (number, prefix,
                  line, postfix, city, state, zip, type, uid))
    conn.commit()
    print_addresses(conn, uid)


def name_editor(uid, fname, lname):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE people SET fname = ?, lname = ? WHERE unique_id = ?', (fname, lname, uid))
    conn.commit()
    print_people(conn, uid)


def phone_editor(uid, mobile, home, work, secondary):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE phone_numbers SET mobile_number = ?, home_number = ?, work_number = ?, '
                 'secondary_number = ? WHERE uid = ?', (mobile, home, work, secondary, uid))
    conn.commit()
    print_phone_numbers(conn, uid)


def notes_editor(uid, note):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE personal_notes SET note = ? WHERE unique_id = ?',
                 (note, uid))
    conn.commit()
    print_personal_notes()



AddressBookDB(db_name).connect()

# name_editor(7, 'i', 'j')