__author__ = 'xi'
import sqlite3

from DBconnector import AddressBookDB


db_name = "yellowpagersdb.db"

def show_address_book():
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_addressbook = conn.execute('select unique_id from people')
    conn.commit()
    for row in cur_addressbook:
        uid = row[0]
        print "uid = ", uid
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)


def by_email(user_in):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_email = conn.execute('select * from email where email = ? ', (user_in))
    conn.commit()
    for row in cur_email:
        uid = row[0]
        print "uid = ", uid
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
    return uid


def by_name(user_in):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_people = conn.execute('select * from people where fname = ? or lname = ?', (user_in, user_in,))
    conn.commit()
    for row in cur_people:
        uid = row[0]
        print "uid = ", uid
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
    return uid



def by_addresses(user_in):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_addresses = conn.execute('select * from addresses where address_line_one = ? or '
                                 'address_line_two = ? or city = ? or state = ?'
                                 'or zip = ? ',
                                 (user_in, user_in,user_in, user_in, user_in,))
    conn.commit()
    for row in cur_addresses:
        uid = row[0]
        print "uid = ", uid
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
    return uid



def by_phone_numbers(user_in):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_phone_numbers = conn.execute('SELECT * from phone_numbers WHERE phone_number = ? ', (user_in,))
    for row in cur_phone_numbers:
        uid = row[0]
        print "uid = ", uid
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
    return uid



def print_email(conn, uid):
    cur_email = conn.execute('select * from email where unique_id = ?', (uid,))
    conn.commit()
    for row in cur_email:
        print "email = ", row[1]


def print_people(conn, uid):
    cur_people = conn.execute('select * from people where unique_id = ?', (uid,))
    conn.commit()
    for row in cur_people:
        print "uid = ", row[0]
        print "fname = ", row[1]
        print "lname = ", row[2]


def print_addresses(conn, uid):
    cur_addresses = conn.execute('select * from addresses where unique_id = ?', (uid,))
    conn.commit()
    for row in cur_addresses:
        print "address_number = ", row[1]
        print "address_prefix = ", row[2]
        print "address_line = ", row[3]
        print "address_postfix = ", row[4]
        print "city = ", row[5]
        print "state = ", row[6]
        print "zip = ", row[7]
        print "type = ", row[8]
        print "data_added = ", row[9]
        print "dare_modified = ", row[10]


def print_phone_numbers(conn, uid):
    cur_phone_numbers = conn.execute('select * from phone_numbers where unique_id = ?', (uid,))
    conn.commit()
    for row in cur_phone_numbers:
        print "phone_numbers = ", row[1]
        print "label = ", row[2]



AddressBookDB(db_name).connect()
