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
        print_people(conn, uid)
        print_email(conn, uid)
        print_phone_numbers(conn, uid)
        print_addresses(conn, uid)
        print_personal_notes(conn, uid)


def show_favorites():
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_favorities = conn.execute('select * from favorites')
    conn.commit()
    for row in cur_favorities:
        print "uid = ", row[0]
        print "fname = ", row[1]
        print "lname = ", row[2]


def show_groups():
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_groups = conn.execute('select * from groups')
    conn.commit()
    for row in cur_groups:
        print "group : ",row[0]
    input_group = raw_input("Please select a group you want to check!")
    cur = conn.execute('SELECT unique_id FROM groups WHERE type = ?', (input_group))
    conn.commit()
    for row in cur:
        uid = row[0];
        print_people(conn, uid)


def by_email(email):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_email = conn.execute('select * from email where primary_email = ? or secondary_email = ? or third_email = ?', (email, email, email))
    conn.commit()
    uid = 0;
    for row in cur_email:
        uid = row[0];
        print "uid = ", row[0]
        print "primary_email = ", row[1]
        print "secondary_email = ", row[2]
        print "third_email = ", row[3]

        print_people(conn, uid);
        print_addresses(conn, uid);
        print_personal_notes(conn, uid);
        print_phone_numbers(conn, uid);
        print_group(conn, uid);



def by_name(fname, lname):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_people = conn.execute('select * from people where fname = ? and lname = ?', (fname, lname))
    conn.commit()
    for row in cur_people:
        uid_s = row[0];
        uid = int(uid_s);
        print "uid =",  row[0]
        print "fname = ", row[1]
        print "lname = ", row[2]
        print "addressbook_code = ", row[3]

        print_email(conn, uid);
        print_addresses(conn, uid);
        print_personal_notes(conn, uid);
        print_phone_numbers(conn, uid);
        print_group(conn, uid);


def by_addresses(address_number, address_prefix, address_line, address_postfix, city, state):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_addresses = conn.execute('select * from addresses where address_number = ? and '
                                 'address_prefix = ? and address_line = ? and address_postfix = ?'
                                 'and city = ? and state = ?',(address_number, address_prefix,address_line,
                                  address_postfix, city, state))
    conn.commit()
    for row in cur_addresses:
        uid = row[0];
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

        print_email(conn, uid);
        print_people(conn, uid);
        print_personal_notes(conn, uid);
        print_phone_numbers(conn, uid);
        print_group(conn, uid);


def by_phone_numbers(phone_number):
    with sqlite3.connect(db_name) as conn:
        conn.cursor()
    cur_phone_numbers = conn.execute('SELECT * from phone_numbers WHERE mobile_number = ? '
                                     'or home_number = ? or work_number = ? or secondary_number = ?',
                                      (phone_number,phone_number,phone_number,phone_number,phone_number))
    for row in cur_phone_numbers:
        uid = row[0];
        print "phone_numbers = ", row[1]
        print "mobile_number  = ", row[2]
        print "home_number = ", row[3]
        print "work_number = ", row[4]
        print "secondary_number = ", row[5]

        print_email(conn, uid);
        print_people(conn, uid);
        print_personal_notes(conn, uid);
        print_addresses(conn, uid);
        print_group(conn, uid);




def print_email(conn, uid):
    cur_email = conn.execute('select * from email where unique_id = ?', (uid,))
    conn.commit()
    for row in cur_email:
        print "primary_email = ", row[1]
        print "secondary_email = ", row[2]
        print "third_email = ", row[3]

def print_people(conn, uid):
    cur_people = conn.execute('select * from people where unique_id = ?',(uid,))
    conn.commit()
    for row in cur_people:
        print "uid = ", row[0]
        print "fname = ", row[1]
        print "lname = ", row[2]
        print "addressbook_code = ", row[3]


def print_addresses(conn, uid):
    cur_addresses = conn.execute('select * from addresses where unique_id = ?',(uid,))
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


def print_personal_notes(conn, uid):
    cur_personal_notes = conn.execute('select * from personal_notes where unique_id = ?',(uid,))
    conn.commit()
    for row in cur_personal_notes:
        print "data_added = ", row[1]
        print "data_modofied  = ", row[2]
        print "note = ", row[3]


def print_phone_numbers(conn, uid):
    cur_phone_numbers = conn.execute('select'
                              ' * from phone_numbers where unique_id = ?',(uid,))
    conn.commit()
    for row in cur_phone_numbers:
        print "phone_numbers = ", row[1]
        print "mobile_number  = ", row[2]
        print "home_number = ", row[3]
        print "work_number = ", row[4]
        print "secondary_number = ", row[5]


def print_group(conn, uid):
    cur_groups = conn.execute('select * from groups where unique_id = ?', (uid,))
    conn.commit()
    for row in cur_groups:
        print("group type = ", row[0])


AddressBookDB(db_name).connect()

# call function here




show_address_book()
# show_favorites()
# by_name("Xi", "Zhang")

# print "please enter a full name for searching!"
# fname = raw_input("enter first name please: ")
# lname = raw_input("enter last name please: ")
# by_name(fname, lname);
#
# print "Wanna figure whose email it is? please enter email for searching! "
# email = raw_input("enter email here: ")
# by_email(email);
