
from Tkinter import *
from Tkinter import Frame, Tk, BOTH, Text, Menu, END
from ttk import Frame, Button, Label, Style
from ttk import Entry
import tkFileDialog
import csv
import os
import shutil
import sqlite3
#import DBdriver
import sys
from People import PeopleTable
from PhoneNumber import PhoneTable
from Address import AddressTable
from Email import EmailTable

db_name = "yellowpagersdb.db"

global nEntry
global p1Entry
global p2Entry
global eEntry
global eEntry2
global aEntry1
global aEntry2
global aEntryc
global aEntrys
global aEntryz
global aEntry12
global aEntry22
global aEntryc2
global aEntrys2
global aEntryz2
global Email
global People
global Phone
global Address
People = PeopleTable(db_name)
Email = EmailTable(db_name)
Phone = PhoneTable(db_name)
Address = AddressTable(db_name)

##Everything is coming out of mainWin now. The other classes are leftover for reference
class mainWin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        #root = Tk()
       # Newcon = initNC(parent)
        self.parent = parent
        self.initUI()
        NC = False
        SC = False
        ST = False

        #self.initNC()

    def initUI(self):
        global nEntry
        global p1Entry
        global p2Entry
        global eEntry
        global eEntry2
        global aEntry1
        global aEntry2
        global aEntryc
        global aEntrys
        global aEntryz
        global aEntry12
        global aEntry22
        global aEntryc2
        global aEntrys2
        global aEntryz2

        self.parent.title("Address Book")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)
        self.rowconfigure(10, pad=3)

        ###Begin Separate Window buttons! E.g. Click new contact and a new window pops up!

        ###
        ### STILL NEEDS AN ONCLICK FUNCTION
        ###

        #Database stuff starts here?
        maintabe = PeopleTable(db_name)


        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Import", command=self.import_tsv)
        fileMenu.add_command(label="Export", command=self.export_tsv)
        fileMenu.add_command(label="Merge", command=self.onOpen)#same as above)
        fileMenu.add_command(label="Print", command=self.onOpen)#once more)
        menubar.add_cascade(label="File", menu=fileMenu)


        ##This is normally the area for buttons, commented out for now

        ##Here's where the problem starts. It's basically you can have buttons or menus.
        ##Having both causes the program to stall out

        ##EDIT: The issue is fixed!

        ##Top row of the main UI
        searB = Button(self, text="Search")
        searB.grid(row=0, column=1)
        sear = Entry(self, width=15) #state=DISABLED)
        sear.grid(row=0,column=0)
        name = Button(self, text="Name")
        name.grid(row=0, column=2)
        #OnClick() -- a quick way to sort alphabetically?
        priPhone = Button(self, text="Primary Phone")
        priPhone.grid(row=0, column=3)
        #OnClick() -- a quick way to sort by the primary phone
        priEmail = Button(self, text="Primary Email")
        priEmail.grid(row=0, column=4)
        #OnClick() -- a quick way to sort by the primary phone
        priAdd = Button(self, text="Primary Address")
        priAdd.grid(row=0, column=5)
        #Onclick() -- a quick way to sort by primary address

        ##First column of the main UI
        #sort = Label(self, text="Sort")
        #sort.grid(row=1, column=0)
        sEdit = Button(self, text="Edit", command=self.onName)
        sEdit.grid(row=2, column=0)
        newcont = Button(self, text="New Contact", command=self.onNC)
        newcont.grid(row=3, column=0)
        sName = Button(self, text="Sort by Name", command=self.onAdd)
        sName.grid(row=4, column=0)
        sZip = Button(self, text="Sort by ZIP", command=self.onZIP)
        sZip.grid(row=5, column=0)



        self.pack()

    def onName(self):
        print("naaaaammmmee")
        ##DO THE DATABASE THINGYMAJIG

    def onPhone(self):
        print("phoooonnee")

    def onEmail(self):
        print("eeeemmaaaiiiiillll")

    def onAdd(self):
        print("address")

    def onZIP(self):
        print("ZIP")

    def onOpen(self):
        file = tkFileDialog.askopenfile(parent=self, mode='r', title='Choose a file')
        if file != None:
            data = file.read()

    def import_tsv(self):
        try:
            file = tkFileDialog.askopenfile(parent=self, mode='rb', filetypes=[('Tab separated values', '*.tsv')],
                                            title='Choose a file to import')
            __file__ = file.name
            pwd = os.path.join(__file__)
            print(pwd)
            abs_path = os.path.abspath(file.name)
            print(abs_path)
            mv = shutil.copy(abs_path, os.getcwd())
            r_csv = csv.reader(open(abs_path, "rb"))
            fhand = open(abs_path)
        except:
            print 'File cannot be opened: ', file.name
            exit()

    def export_tsv(self):
        try:
            file = tkFileDialog.asksaveasfile(parent=self, mode='wb', defaultextension=".tsv")
            __file__ = file.name
            pwd = os.path.join(__file__)
            print(pwd)
            print(os.getcwd())
            w_csv = csv.writer(open(pwd, "wb"))
            with open(pwd, "wb") as output:
                output.write('need to integrate to export the database')
        except:
            print 'File cannot be saved: ', file.name
            exit()

    def onNC(self):
        global nEntry
        global p1Entry
        global p2Entry
        global eEntry
        global eEntry2
        global aEntry1
        global aEntry2
        global aEntryc
        global aEntrys
        global aEntryz
        global aEntry12
        global aEntry22
        global aEntryc2
        global aEntrys2
        global aEntryz2
        dialog = Toplevel(self, background="#c3f6f7")
        #dialog.geometry("300x250+300+300")
        dialog.wm_title("New Contact")
        #dialog.configure(bg="blue")
        dialog.wm_transient(self)
        #dialog.wm_protocol("WM_DELETE_WINDOW", lambda: self.onSave(dialog))
        '''dialog.columnconfigure(0, pad=3)
        dialog.columnconfigure(1, pad=3)
        dialog.columnconfigure(2, pad=3)
        dialog.columnconfigure(3, pad=3)
        dialog.columnconfigure(4, pad=3)
        dialog.columnconfigure(5, pad=3)
        dialog.columnconfigure(6, pad=3)
        dialog.columnconfigure(7, pad=3)
        dialog.columnconfigure(8, pad=3)

        dialog.rowconfigure(0, pad=3)
        dialog.rowconfigure(1, pad=3)
        dialog.rowconfigure(2, pad=3)
        dialog.rowconfigure(3, pad=3)
        '''




        #Text boxes for entering name, address, phone, and email
        nLabel = Label(dialog, text="Enter Name:", background="#c3f6f7")
        #nLabel.configure(background="blue")
        #self.instruction.configure()
        nLabel.grid(row=1, column=1,sticky=W)
        nEntry = Entry(dialog)
        nEntry.grid(row=1,column=2, columnspan=2)


        self.instruction = Label(dialog, text="Enter Phone:")
        self.instruction.grid(row=2, column=1,sticky=W)
        p1Entry = Entry(dialog)
        p1Entry.grid(row=2, column=2, columnspan=2)

        self.instruction = Label(dialog, text="Enter Email:")
        self.instruction.grid(row=3, column=1, sticky=W)
        eEntry = Entry(dialog)
        eEntry.grid(row=3, column=2, columnspan=2)

        self.instruction = Label(dialog, text="Address Line 1:")
        self.instruction.grid(row=1, column=4)
        aEntry1 = Entry(dialog, width=50)
        aEntry1.grid(row=1, column=5, columnspan=5)

        self.instruction = Label(dialog, text="Address Line 2:")
        self.instruction.grid(row=2, column=4)
        aEntry2 = Entry(dialog, width=50)
        aEntry2.grid(row=2, column=5, columnspan=5)

        self.instruction = Label(dialog, text="City:")
        self.instruction.grid(row=3, column=4)
        aEntryc = Entry(dialog)
        aEntryc.grid(row=3, column=5)

        self.instruction = Label(dialog, text="State")
        self.instruction.grid(row=3, column=6)
        aEntrys = Entry(dialog, width=4)
        aEntrys.grid(row=3, column=7)

        self.instruction = Label(dialog, text="ZIP:")
        self.instruction.grid(row=3, column=8)
        aEntryz = Entry(dialog, width=12)
        aEntryz.grid(row=3, column=9)

        plusP = Button(dialog, text="+Phone", command=self.onplusP)
        plusP.grid(row=1, column=10)
        plusA = Button(dialog, text="+Address", command=self.onplusA)
        plusA.grid(row=2, column=10)
        plusE = Button(dialog, text="+Email", command=self.onplusE)
        plusE.grid(row=3, column=10)

        #button = Button(dialog, text="Close", command=lambda: self.onSave(dialog))
        #button.grid()
        save = Button(dialog, text="Save", command=lambda: self.onSave(dialog))
        save.grid(row=1, column=11)
        #self.pack()
        return nEntry, p1Entry, eEntry, aEntry1, aEntry2, aEntryc, aEntrys, aEntryz



    def onSC(self):
        SC = True
        self.initSC()
    def onST(self):
        ST = True
        self.initST()
    def initSC(self):
        self.parent.title("Search by:")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)


        sName = Label(self, text="Name")
        sName.grid(row=0, column=0)
        #OnClick()

        seName = Entry(self)
        seName.grid(row=0, column=1)

        #sAdd = Label(self, text="Address")
        #sAdd.grid(row=0, column=1)
        #OnClick()


        sZip = Label(self, text="ZIP")
        sZip.grid(row=0, column=2)
        #OnClick()

        sPh = Label(self, text="Phone")
        sPh.grid(row=1, column=0)
        #OnClick()

        sEm = Label(self, text="Email")
        sEm.grid(row=1, column =1)
        #OnClick()

        sGr = Label(self, text="Groups")
        sGr.grid(row=1, column=2)
        #OnClick()

        self.pack()
    def initNC(self):
        self.parent.title("New Contact")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)
        self.columnconfigure(5, pad=3)
        self.columnconfigure(6, pad=3)
        self.columnconfigure(7, pad=3)
        self.columnconfigure(8, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)

        #Text boxes for entering name, address, phone, and email
        self.instruction = Label(self, text="Enter Name:")
        self.instruction.grid(row=1, column=1,sticky=W)
        nEntry = Entry(self)
        nEntry.grid(row=1,column=2, columnspan=2)


        self.instruction = Label(self, text="Enter Phone:")
        self.instruction.grid(row=2, column=1,sticky=W)
        p1Entry = Entry(self)
        p1Entry.grid(row=2, column=2, columnspan=2)

        self.instruction = Label(self, text="Enter Email:")
        self.instruction.grid(row=3, column=1, sticky=W)
        eEntry = Entry(self)
        eEntry.grid(row=3, column=2, columnspan=2)

        self.instruction = Label(self, text="Address Line 1:")
        self.instruction.grid(row=1, column=4)
        aEntry1 = Entry(self, width=50)
        aEntry1.grid(row=1, column=5, columnspan=5)

        self.instruction = Label(self, text="Address Line 2:")
        self.instruction.grid(row=2, column=4)
        aEntry2 = Entry(self, width=50)
        aEntry2.grid(row=2, column=5, columnspan=5)

        self.instruction = Label(self, text="City:")
        self.instruction.grid(row=3, column=4)
        aEntryc = Entry(self)
        aEntryc.grid(row=3, column=5)

        self.instruction = Label(self, text="State")
        self.instruction.grid(row=3, column=6)
        aEntrys = Entry(self, width=4)
        aEntrys.grid(row=3, column=7)

        self.instruction = Label(self, text="ZIP:")
        self.instruction.grid(row=3, column=8)
        aEntryz = Entry(self, width=12)
        aEntryz.grid(row=3, column=9)

        plusP = Button(self, text="+Phone", command=self.onplusP)
        plusP.grid(row=1, column=10)
        plusA = Button(self, text="+Address", command=self.onplusA)
        plusA.grid(row=2, column=10)
        plusE = Button(self, text="+Email", command=self.onplusE)
        plusE.grid(row=3, column=10)

        save = Button(self, text="Save", command=self.onSave)
        save.grid(row=1, column=11)

        #top =
        #handle = lambda: self.onNCC(top)
        #conf = Button(self, text="Confirm", command=handle)
        #conf.grid(row=2, column=7)

        self.pack()
        return nEntry, p1Entry, eEntry, aEntry1, aEntry2, aEntryc, aEntrys, aEntryz
    def onplusP(self):
        #Database stuff starts here?
        #maintabe = PeopleTable(db_name)
        self.instruction = Label(self, text="Enter Phone:")#, command=maintabe.insert_people)
        self.instruction.grid(column=1,sticky=W)
        p2Entry = Entry(self)
        p2Entry.grid(column=2)
    def onplusE(self):
        self.instruction = Label(self, text="Enter Email:")
        self.instruction.grid(column=1, sticky=W)
        eEntry2 = Entry(self)
        eEntry2.grid(column=2)
    def onplusA(self):
        self.instruction = Label(self, text="Address Line 1:")
        self.instruction.grid( column=4)
        aEntry12 = Entry(self, width=50)
        aEntry12.grid(column=5, columnspan=5)

        self.instruction = Label(self, text="Address Line 2:")
        self.instruction.grid( column=4)
        aEntry22 = Entry(self, width=50)
        aEntry22.grid(column=5, columnspan=5)

        self.instruction = Label(self, text="City:")
        self.instruction.grid( column=4)
        aEntryc2 = Entry(self)
        aEntryc2.grid(column=5)

        self.instruction = Label(self, text="State")
        self.instruction.grid(column=6)
        aEntrys2 = Entry(self, width=4)
        aEntrys2.grid(column=7)

        self.instruction = Label(self, text="ZIP:")
        self.instruction.grid(column=8)
        aEntryz2 = Entry(self, width=12)
        aEntryz2.grid(column=9)
    def onSave(self, w):
        global nEntry
        global p1Entry
        global p2Entry
        global eEntry
        global eEntry2
        global aEntry1
        global aEntry2
        global aEntryc
        global aEntrys
        global aEntryz
        global aEntry12
        global aEntry22
        global aEntryc2
        global aEntrys2
        global aEntryz2

        name1 = nEntry.get()
        phone1 = p1Entry.get()
        email1 = eEntry.get()
        #print(name1)
        ##Initial stuff
        global People
        global Email
        global Phone
        global Address
        a = People.insert_people(name1, name1)
        b = Phone.insert_phone(a, phone1)
        c = Email.insert_email(a, email1)
        #d = People.delete_people(a)
        #e = Phone.delete_phone(a)
        #f = Email.delete_email(a)
        #Address.insert_address()
        w.destroy()



        #EDIT, DO THE DATABASE THINGYMAJIG
    def initST(self):
        self.parent.title("Sort by:")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        sName = Button(self, text="Name")
        sName.grid(row=1, column=0)
        #OnClick()

        sAdd = Button(self, text="Address")
        sAdd.grid(row=2, column=0)
        #OnClick()

        sZip = Button(self, text="ZIP")
        sZip.grid(row=3, column=0)
        #OnClick()

        sPh = Button(self, text="Phone")
        sPh.grid(row=4, column=0)
        #OnClick()

        sEm = Button(self, text="Email")
        sEm.grid(row=5, column=0)
        #OnClick()

        sGr = Button(self, text="Groups")
        sGr.grid(row=6, column=0)
        #OnClick()

        self.pack()

def main():
    root = Tk()
    root.config(bg='#c3f6f7')
    #main UI window root
    #root.geometry("300x250+300+300")
    #root1 = Tk()
    #root2 = Tk()
    #root3 = Tk()
    #root4 = Tk()
    #root5 = Tk()
    #root6 = Tk()

    #imdb = openDB(root2) #-- #open file dialogue
    #app = dialPad(root1) #- #dialpad
    #sear = search(root3) #search popup
    #sor = sort(root4) #sort popup
    wind = mainWin(root) #Main window
    #newc = newContact(root1) #new contact
    #viewc = viewCon(root6) #view contact
    root.mainloop() #Init root
    #root1.mainloop()


if __name__ == '__main__':
    main()