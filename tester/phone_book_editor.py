__author__ = 'xi'

import sqlite3
from DBconnector import AddressBookDB
from searching_driver import *


db_name = "yellowpagersdb.db"

def email_editor(uid, email):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE email SET email = ? '
                 'WHERE unique_id = ?', (email, uid))
    conn.commit()
    print_email(conn, uid)
    return uid


def address_editor(uid, line_one, line_two, city, state, zip):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE addresses SET address_line_one = ?, address_line_two = ?, '
                 'city = ?, state = ?, zip = ?, type = ? '
                 'WHERE unique_id = ?', (line_one, line_two,
                   city, state, zip, type, uid))
    conn.commit()
    print_addresses(conn, uid)
    return uid


def name_editor(uid, fname, lname):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE people SET fname = ?, lname = ? WHERE unique_id = ?', (fname, lname, uid))
    conn.commit()
    print_people(conn, uid)
    return uid


def phone_editor(uid, phone):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    conn.execute('UPDATE phone_number SET phone_number = ?'
                 'WHERE uid = ?', (phone, uid))
    conn.commit()
    print_phone_numbers(conn, uid)



AddressBookDB(db_name).connect()

# name_editor(7, 'i', 'j')