__author__ = 'Victoria'

import os
import sqlite3

db_filename = "yellowpagersdb"

db_new = not os.path.exists(db_filename)

# conn = sqlite3.connect(db_filename)

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

if db_new:
    print 'Need to create a schema'
else:
    print 'Database already exists'

# need to make this so its dynamic
def insertPeople():
    conn.execute("insert into people(unique_id, fname, lname, addressbook_code) \
            values(9, 'Mike', 'Brown', 'TST')")

def deletePeople():
    conn.execute("delete from people where unique_id = 9")
    conn.commit


insertPeople()

cursor = conn.execute("select unique_id, fname, lname, addressbook_code from people")

for row in cursor:
    print "unique_id = ", row[0]
    print "fname = ", row[1]
    print "lname = ", row[2]
    print "addressbook_code = ", row[3], "\n"

deletePeople()

print "Total number of rows deleted: ", conn.total_changes

cursor = conn.execute("select unique_id, fname, lname, addressbook_code from people")

for row in cursor:
    print "unique_id = ", row[0]
    print "fname = ", row[1]
    print "lname = ", row[2]
    print "addressbook_code = ", row[3], "\n"

print "finished successfully!"
conn.close()