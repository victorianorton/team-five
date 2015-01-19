__author__ = 'Victoria'
# Database for The YellowPagers address book v0.1

from DBconnector import AddressBookDB
from People import PeopleTable

db_name = "yellowpagersdb"

AddressBookDB(db_name).connect()

PeopleTable(db_name).print_result()

PeopleTable(db_name).insert_people()

PeopleTable(db_name).print_result()

PeopleTable(db_name).delete_people()

AddressBookDB(db_name).close_conn()
