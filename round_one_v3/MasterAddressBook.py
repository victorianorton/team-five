__author__ = 'Victoria'

from tkinter import *
from guiwidgets.listview import MultiListbox
from toolbar import _init_toolbar
from toolbar import _init_sortbyzip
from toolbar import _init_userfield
import sql


class MasterAddressBook:
    # A window with toolbar and displays all the information of the address book
    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        _init_sortbyzip(self)
        _init_userfield(self)
        self._init_gridbox()
        self.form_insert = None
        self.form_edit = None
        self.flag_insert = False
        self.btn_sort_name = None
        self.btn_sort_zip = None
        self.btnuser = None

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('uid', 5), ('First Name', 25), ('Last Name', 25), ('Phone Number', 25),
                                             ('Label', 25), ('Address Line 1', 30), ('Address Line 2', 30), ('City', 10),
                                             ('State', 25), ('Zip', 10), ('Label', 10), ('Email', 25), ('Label', 25)))
        master_tb = sql.session._query("select * from master")
        self.update_mlb(master_tb)
        self.mlb.pack(expand=YES, fill=BOTH)

    # insert button has been clicked
    def btn_insert_click(self):
        if self.flag_insert:
            return 0
        self.flag_insert = True
        self.form_insert = InsertIntoTable()
        self.frame.wait_window(self.form_insert.frame)
        if self.form_insert.ok_btn_clicked == 1:
            tbMaster = sql.session._query("select * from master")
            self.update_mlb(tbMaster)
        self.flag_insert = False

    def btn_edit_click(self):
        print('edit')

    # delete button clicked()
    def btn_del_click(self):
        if self.mlb.item_selected == None:
            return 'please select first'
        print(self.mlb.item_selected[1])
        sql.session.delete_person(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None

    def btn_search_click(self):
        fnd = self.entryfind.get()
        tb_master = sql.session.search_tb(fnd)
        self.update_mlb(tb_master)


    # really werid bug here when sort tries to update its just none even though it prints values at first
    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        print(tb)
        for row in tb:
            self.mlb.insert(END, (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                  row[10], row[11], row[12]))

    def btn_sort_name_click(self):
        print("sort me!")
        tb_master = sql.session.sort_by_name()
        self.update_mlb(tb_master)

    def btn_sort_zip_click(self):
        print("sort zip!")
        tb_master = sql.session.sorting_by_zip()
        self.update_mlb(tb_master)

    def btn_userfield_click(self, feild):
        print("+ User field!")
        UserTop()
        #feild = 'fuckyeah'
        tb_master = sql.session.add_user_feild(feild)
        #self.update_mlb(tb_master)


class InsertIntoTable:
    # Add new person labels and textboxes and an okay button
    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)
        self._init_widgets()

    def _init_widgets(self):
        self.entry1 = Entry(self.frame, width=60)
        self.entry1.insert(0, "First Name")
        self.entry1.grid(row=0, column=0, columnspan=3)
        self.entry1.bind("<FocusIn>", self.clearFnameField)

        self.entry2 = Entry(self.frame, width=60)
        self.entry2.insert(0, "Last Name")
        self.entry2.grid(row=1, column=0, columnspan=3)
        self.entry2.bind("<FocusIn>", self.clearLnameField)

        self.entry3 = Entry(self.frame)
        self.entry3.insert(0, "Phone Number")
        self.entry3.grid(row=2, column=0)
        self.entry3.bind("<FocusIn>", self.clearPhoneField)

        self.entry4 = Entry(self.frame, width=16)
        self.entry4.insert(0, "Phone Label")
        self.entry4.grid(row=2, column=1)
        self.entry4.bind("<FocusIn>", self.clearPhoneLblField)

        self.entry5 = Entry(self.frame)
        self.entry5.insert(0, "Address Line 1")
        self.entry5.grid(row=2, column=2)
        self.entry5.bind("<FocusIn>", self.clearAdd1Field)

        self.entry6 = Entry(self.frame, width=60)
        self.entry6.insert(0, "Address Line 2")
        self.entry6.grid(row=3, column=0, columnspan=3)
        self.entry6.bind("<FocusIn>", self.clearAdd2Field)

        self.entry7 = Entry(self.frame, width=60)
        self.entry7.insert(0, "City")
        self.entry7.grid(row=4, column=0, columnspan=3)
        self.entry7.bind("<FocusIn>", self.clearCityField)

        self.entry8 = Entry(self.frame, width=60)
        self.entry8.insert(0, "State")
        self.entry8.grid(row=5, column=0, columnspan=3)
        self.entry8.bind("<FocusIn>", self.clearStateField)

        self.entry9 = Entry(self.frame)
        self.entry9.insert(0, "Zip")
        self.entry9.grid(row=5, column=0)
        self.entry9.bind("<FocusIn>", self.clearZipField)

        self.entry10 = Entry(self.frame, width=16)
        self.entry10.insert(0, "Address Label")
        self.entry10.grid(row=6, column=1)
        self.entry10.bind("<FocusIn>", self.clearAddLblField)

        self.entry11 = Entry(self.frame)
        self.entry11.insert(0, "Email")
        self.entry11.grid(row=6, column=2)
        self.entry11.bind("<FocusIn>", self.clearEmailField)

        self.entry12 = Entry(self.frame, width=60)
        self.entry12.insert(0, "Email Label")
        self.entry12.grid(row=8, column=0, columnspan=3)
        self.entry12.bind("<FocusIn>", self.clearEmLblField)

        self.entry13 = Entry(self.frame, width=60)
        self.entry13.insert(0, "Custom")
        self.entry13.grid(row=8, column=0, columnspan=3)
        self.entry13.bind("<FocusIn>", self.clearCustomField)

        self.btn_ok = Button(self.frame, text="OK", width=7, command=self.btn_ok_click)
        self.btn_ok.grid(row=9, column=1, sticky=E)

        self.btn_ok = Button(self.frame, text="UPDATE", width=7, command=self.btn_up_click)
        self.btn_ok.grid(row=9, column=1, sticky=W)

    def btn_ok_click(self):
        items = (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(),
                 self.entry6.get(), self.entry7.get(), self.entry8.get(), self.entry9.get(), self.entry10.get(),
                 self.entry11.get(), self.entry12.get())
        if '' in items:
            print('please fill all boxes')
            return 'break'
        sql.session.insert_tb(items)

        self.ok_btn_clicked = 1

        print('user exits the screen by clicking ok button')
        self.frame.destroy()

    def btn_up_click(self):
        items = (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry2.get(),
                 self.entry5.get(), self.entry6.get(), self.entry7.get(), self.entry8.get(), self.entry9.get(),
                 self.entry10.get(), self.entry11.get(), self.entry12.get(), self.entry13.get())
        if '' in items:
            print('please fill all boxes')
            return 'break'
        sql.session.insert_tb(items)

        self.ok_btn_clicked = 1

        print('user exits the screen by clicking ok button')
        self.frame.destroy()

    def callback(self):
        self.ok_btn_clicked = 0
        print('user exits the screen')
        self.frame.destroy()

    def clearFnameField(self, event):
        self.entry1.delete(0,END)

    def clearLnameField(self, event):
        self.entry2.delete(0,END)

    def clearPhoneField(self, event):
        self.entry3.delete(0,END)

    def clearPhoneLblField(self, event):
        self.entry4.delete(0,END)

    def clearAdd1Field(self, event):
        self.entry5.delete(0, END)

    def clearAdd2Field(self, event):
        self.entry6.delete(0, END)

    def clearCityField(self, event):
        self.entry7.delete(0, END)

    def clearStateField(self, event):
        self.entry8.delete(0,END)

    def clearZipField(self, event):
        self.entry9.delete(0,END)

    def clearAddLblField(self, event):
        self.entry10.delete(0,END)

    def clearEmailField(self, event):
        self.entry11.delete(0,END)

    def clearEmLblField(self, event):
        self.entry12.delete(0, END)

    def clearCustomField(self, event):
        self.entry13.delete(0, END)


class UserTop:
    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)
        self._init_widgets()

    def _init_widgets(self):
        self.entry1 = Entry(self.frame, width=60)
        self.entry1.insert(0, "Custom")
        self.entry1.grid(row=0, column=0, columnspan=3)
        self.entry1.bind("<FocusIn>", self.clearEnt)

        self.button = Button(self.frame, text="Okay", width=60, command=self.callback)
        self.button.grid(row=1, column=1)

    def clearEnt(self):
        self.entry1.delete(0,END)

    def callback(self):
        print('user exits the screen')
        self.frame.destroy()


'''class EditTable:

    # Add new person labels and textboxes and an okay button
    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)
        self._init_widgets()

    def _init_widgets(self):

        self.label1 = Label(self.frame, text="UID ")
        self.label1.grid(row=0, sticky=W)
        self.entry1 = Entry(self.frame)
        self.entry1.grid(row=1, column=0)


        self.label2 = Label(self.frame, text="First Name")
        self.label2.grid(row=0, column=1, sticky=W)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=1, column=1)

        self.label3 = Label(self.frame, text="Last Name")
        self.label3.grid(row=2, sticky=W, columnspan=2)
        self.entry3 = Entry(self.frame)
        self.entry3.grid(row=3, sticky=W+E, columnspan=2)


        self.entry1 = Entry(self.frame, width=60)
        self.entry1.insert(0, "First Name")
        self.entry1.grid(row=0, column=0, columnspan=3)
        self.entry1.bind("<FocusIn>", self.clearnamefField)

        self.entry2 = Entry(self.frame, width=60)
        self.entry2.insert(0, "Last Name")
        self.entry2.grid(row=1, column=0, columnspan=3)
        self.entry2.bind("<FocusIn>", self.clearnamelField)

        self.entry3 = Entry(self.frame)
        self.entry3.insert(0, "Phone Number")
        self.entry3.grid(row=2, column=0)
        self.entry3.bind("<FocusIn>", self.clearPhoneField)

        self.entry4 = Entry(self.frame, width=16)
        self.entry4.insert(0, "Phone Label")
        self.entry4.grid(row=2, column=1)
        self.entry4.bind("<FocusIn>", self.clearPhoneLblField)

        self.entry5 = Entry(self.frame)
        self.entry5.insert(0, "Address Line 1")
        self.entry5.grid(row=2, column=2)
        self.entry5.bind("<FocusIn>", self.clearAdd1Field)

        self.entry6 = Entry(self.frame, width=60)
        self.entry6.insert(0, "Address Line 2")
        self.entry6.grid(row=3, column=0, columnspan=3)
        self.entry6.bind("<FocusIn>", self.clearAdd2Field)

        self.entry7 = Entry(self.frame, width=60)
        self.entry7.insert(0, "City")
        self.entry7.grid(row=4, column=0, columnspan=3)
        self.entry7.bind("<FocusIn>", self.clearCityField)

        self.entry8 = Entry(self.frame, width=40)
        self.entry8.insert(0, "State")
        self.entry8.grid(row=5, column=0, columnspan=2)
        self.entry8.bind("<FocusIn>", self.clearStateField)

        self.entry9 = Entry(self.frame)
        self.entry9.insert(0, "Zip")
        self.entry9.grid(row=5, column=2)
        self.entry9.bind("<FocusIn>", self.clearZipField)

        self.entry10 = Entry(self.frame, width=16)
        self.entry10.insert(0, "Address Label")
        self.entry10.grid(row=6, column=1)
        self.entry10.bind("<FocusIn>", self.clearAddLblField)

        self.entry11 = Entry(self.frame)
        self.entry11.insert(0, "Email")
        self.entry11.grid(row=6, column=2)
        self.entry11.bind("<FocusIn>", self.clearEmailField)

        self.entry12 = Entry(self.frame, width=60)
        self.entry12.insert(0, "Email Label")
        self.entry12.grid(row=7, column=0, columnspan=3)
        self.entry12.bind("<FocusIn>", self.clearEmLblField)

        self.entry13 = Entry(self.frame, width=60)
        self.entry13.insert(0, "Custom")
        self.entry13.grid(row=8, column=0, columnspan=3)
        self.entry13.bind("<FocusIn>", self.clearCustomField)

        self.btn_ok = Button(self.frame, text="UPDATE", width=7, command=self.btn_up_click)
        self.btn_ok.grid(row=9, column=0, sticky=W)

    def btn_up_click(self):
        #items = (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(),
                ## self.entry5.get(), self.entry6.get(), self.entry7.get(), self.entry8.get(), self.entry9.get(),
                 #self.entry10.get(), self.entry11.get(), self.entry12.get(), self.entry13.get())
        #if '' in items:
         #   print('please fill all boxes')
         #   return 'break'
        #print(items)
       # sql.session.insert_tb(items)

        if self.entry1.get() and self.entry2.get():
            print("editing name!")
            fname=self.entry1.get()
            lname=self.entry2.get()
            sql.session.name_editor(fname, lname)



        self.ok_btn_clicked = 1

        print('user exits the screen by clicking ok button')
        self.frame.destroy()

    def callback(self):
        self.ok_btn_clicked = 0
        print('user exits the screen')
        self.frame.destroy()

    def clearnamefField(self, event):
        self.entry1.delete(0,END)

    def clearnamelField(self, event):
        self.entry2.delete(0,END)

    def clearPhoneField(self, event):
        self.entry3.delete(0,END)

    def clearPhoneLblField(self, event):
        self.entry4.delete(0,END)

    def clearAdd1Field(self, event):
        self.entry5.delete(0, END)

    def clearAdd2Field(self, event):
        self.entry6.delete(0, END)

    def clearCityField(self, event):
        self.entry7.delete(0, END)

    def clearStateField(self, event):
        self.entry8.delete(0,END)

    def clearZipField(self, event):
        self.entry9.delete(0,END)

    def clearAddLblField(self, event):
        self.entry10.delete(0,END)

    def clearEmailField(self, event):
        self.entry11.delete(0,END)

    def clearEmLblField(self, event):
        self.entry12.delete(0, END)

    def clearCustomField(self, event):


       self.entry13.delete(0, END)
       '''