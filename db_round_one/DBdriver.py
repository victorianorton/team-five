__author__ = 'Victoria'

from DBconnector import AddressBookDB
from People import PeopleTable
from Email import EmailTable
from Favorite import FavoriteTable
from Group import GroupTable
from Master import MasterTable
from Personal_Notes import NoteTable
from PhoneNumber import PhoneTable
from Search import SearchTable
from Address import AddressTable

db_name = "yellowpagersdb"


def p_menu():
    print('Please look at the following options: \n'
          '0 to print all the people\n'
          '1 to insert a name\n'
          '2 to delete a name\n'
          '3 to insert an email\n'
          '4 to delete an email\n'
          '5 to insert a favorite\n'
          '6 to delete a favorite\n'
          '7 to create a group\n'
          '8 to delete a group\n'
          '9 to create a master address book\n'
          '10 to delete a master address book\n'
          '11 to create a personal note\n'
          '12 to delete a personal note\n'
          '13 to insert phone number\n'
          '14 to delete phone number\n'
          '15 to insert a search (should prolly delete this one)\n'
          '16 to delete a past search\n'
          '17 to print all the emails\n'
          '18 to print all the favorites\n'
          '19 to print all the groups\n'
          '20 to print all the master address books\n'
          '21 to print all the personal notes\n'
          '22 to print all the phone numbers\n'
          '23 to print all the past searches (not working yet)\n'
          '24 to print all the addresses\n'
          '25 to insert an address\n'
          '26 to delete an address\n'
          '27 to repeat this menu\n'
          '28 to exit\n')


def p_people():
    PeopleTable(db_name).print_result()


def i_people():
    PeopleTable(db_name).insert_people()


def d_people():
    PeopleTable(db_name).delete_people()


def p_email():
    EmailTable(db_name).print_email_result()


def i_email():
    EmailTable(db_name).insert_email()


def d_email():
    EmailTable(db_name).delete_email()


def p_favorite():
    FavoriteTable(db_name).print_favorite_result()


def i_favorite():
    FavoriteTable(db_name).insert_favorite()


def d_favorite():
    FavoriteTable(db_name).delete_favorite()


def p_group():
    GroupTable(db_name).print_group_result()


def i_group():
    GroupTable(db_name).insert_group()


def d_group():
    GroupTable(db_name).delete_group()


def p_master():
    MasterTable(db_name).print_master_result()


def i_master():
    MasterTable(db_name).insert_master()


def d_master():
    MasterTable(db_name).delete_master()


def p_note():
    NoteTable(db_name).print_note_result()


def i_note():
    NoteTable(db_name).insert_note()


def d_note():
    NoteTable(db_name).delete_note()


def p_phone():
    PhoneTable(db_name).print_phone_result()


def i_phone():
    PhoneTable(db_name).insert_phone()


def d_phone():
    PhoneTable(db_name).delete_phone()


def p_search():
    SearchTable(db_name).print_search_result()


def i_search():
    SearchTable(db_name).insert_search()


def d_search():
    SearchTable(db_name).delete_search()


def p_address():
    AddressTable(db_name).print_address_result()


def i_address():
    AddressTable(db_name).insert_address()


def d_address():
    AddressTable(db_name).delete_address()


def c_close():
    AddressBookDB(db_name).close_conn()


AddressBookDB(db_name).connect()
p_menu()

x = int(raw_input('Please choose from menu: '))

print x
if x == 0:
    p_people()
if x == 1:
    i_people()
if x == 2:
    d_people()
if x == 3:
    i_email()
if x == 4:
    d_email()
if x == 5:
    i_favorite()
if x == 6:
    d_favorite()
if x == 7:
    i_group()
if x == 8:
    d_group()
if x == 9:
    i_master()
if x == 10:
    d_master()
if x == 11:
    i_note()
if x == 12:
    d_note()
if x == 13:
    i_phone()
if x == 14:
    d_phone()
if x == 15:
    i_search()
if x == 16:
    d_search()
if x == 17:
    p_email()
if x == 18:
    p_favorite()
if x == 19:
    p_group()
if x == 20:
    p_master()
if x == 21:
    p_note()
if x == 22:
    p_phone()
if x == 23:
    p_search()
if x == 24:
    p_address()
if x == 25:
    i_address()
if x == 26:
    d_address()
else:
    c_close()