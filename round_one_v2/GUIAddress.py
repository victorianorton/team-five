__author__ = 'Victoria'

from tkinter import *
from guiwidgets.listview import MultiListbox
from blackbox import _init_toolbar
import sql

                            # Declare a list for the Entry widgets.


class Address:
    # email window with toolbar and a data grid of emails and people names
    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        self._init_gridbox()
        self.frm_insert_phone = None
        self.frm_edit_phone = None
        self.add_phone_flag = False

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('UID', 3), ('Address Line 1', 50), ('Address Line 2', 50), ('City', 25),
                                             ('State', 25), ('Zip', 10), ('Label', 25)))
        tb_address = sql.session._query("select * from addresses ")
        self.update_mlb(tb_address)
        self.mlb.pack(expand=YES, fill=BOTH)

    # insert_phone button clicked()
    def btn_add_click(self):
        if self.add_phone_flag:
            return 0
        self.add_address_flag = True
        self.frm_insert_address = AddAddress()
        self.frame.wait_window(self.frm_insert_address.frame)
        if self.frm_insert_address._okbtn_clicked == 1:
            tbAddress = sql.session._query("select * from addresses")
            self.update_mlb(tbAddress)
        self.add_phone_flag = False

    def btn_edit_click(self):
        print('edit')

    # delete_people button clicked()
    def btn_del_click(self):
        if self.mlb.item_selected == None:
            return 'please select first'
        print(self.mlb.item_selected[1])
        sql.session.delete_address(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None

    def btn_search_click(self):
        fnd = self.entryfind.get()

        tb_address = sql.session.search_address(fnd)
        self.update_mlb(tb_address)

    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        for row in tb:
            self.mlb.insert(END, (int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6]))


class AddAddress:
    # Add new email labels and textboxes and an OK button
    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)
        self._init_widgets()

    def _init_widgets(self):
        self.entry1 = Entry(self.frame, width=60)
        self.entry1.insert(0, "Address Line 1")
        self.entry1.grid(row=0, column=0, columnspan=3)

        self.entry2 = Entry(self.frame, width=60)
        self.entry2.insert(0, "Address Line 2")
        self.entry2.grid(row=1, column=0, columnspan=3)

        self.entry3 = Entry(self.frame)
        self.entry3.insert(0, "City")
        self.entry3.grid(row=2, column=0)

        self.entry4 = Entry(self.frame, width=16)
        self.entry4.insert(0, "State")
        self.entry4.grid(row=2, column=1)

        self.entry5 = Entry(self.frame)
        self.entry5.insert(0, "ZIP")
        self.entry5.grid(row=2, column=2)

        self.entry6 = Entry(self.frame, width=60)
        self.entry6.insert(0, "Label")
        self.entry6.grid(row=3, column=0, columnspan=3)


        self.btn_ok = Button(self.frame, text="OK", width=7, command=self.btnok_click)
        self.btn_ok.grid(row=4, column=2, sticky=E)

    def callback(event):
        global clicked
        if (clicked == False):
            # box[0].delete(0, END)         #
            # box[0].config(fg = "black")   # Change the colour of the text here.
            clicked = True

    def btnok_click(self):
        items = (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get())
        if '' in items:
            print('please fill all boxes')
            return 'break'
        sql.session.insert_address(items)

        self._okbtn_clicked = 1
        print('user exits the screen by clicking ok button')
        self.frame.destroy()

    def callback(self):

        self._okbtn_clicked = 0
        print('user exits the screen')
        self.frame.destroy()
