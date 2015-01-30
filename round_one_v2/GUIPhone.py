__author__ = 'Victoria'

from tkinter import *
from guiwidgets.listview import MultiListbox
from blackbox import _init_toolbar
import sql


class PhoneNumber:
    # email window with toolbar and a data grid of emails and people names
    def __init__(self):
        self.frame = Toplevel()
        _init_toolbar(self)
        self._init_gridbox()
        self.frm_insert_phone = None
        self.frm_edit_phone = None
        self.add_phone_flag = False

    def _init_gridbox(self):
        self.mlb = MultiListbox(self.frame, (('UID', 3), ('Phone Number', 25), ('Label', 25)))
        tb_phone = sql.session._query("select * from phone_numbers ")
        self.update_mlb(tb_phone)
        self.mlb.pack(expand=YES, fill=BOTH)

    # insert_phone button clicked()
    def btn_add_click(self):
        if self.add_phone_flag:
            return 0
        self.add_phone_flag = True
        self.frm_insert_phone = AddPhoneNumber()
        self.frame.wait_window(self.frm_insert_phone.frame)
        if self.frm_insert_phone._okbtn_clicked == 1:
            tbPhone = sql.session._query("select * from phone_numbers")
            self.update_mlb(tbPhone)
        self.add_phone_flag = False

    def btn_edit_click(self):
        print('edit')

    # delete_people button clicked()
    def btn_del_click(self):
        if self.mlb.item_selected == None:
            return 'please select first'
        print(self.mlb.item_selected[1])
        sql.session.delete_phone(int(self.mlb.item_selected[1]))
        self.mlb.delete(self.mlb.item_selected[0])
        self.mlb.item_selected = None

    def btn_search_click(self):
        fnd = self.entryfind.get()

        tb_phone = sql.session.search_phone(fnd)
        self.update_mlb(tb_phone)

    def update_mlb(self, tb):
        self.mlb.delete(0, END)
        for row in tb:
            self.mlb.insert(END, (int(row[0]), row[1], row[2]))


class AddPhoneNumber:
    # Add new email labels and textboxes and an OK button
    def __init__(self):
        self.frame = Toplevel()
        self.frame.protocol("WM_DELETE_WINDOW", self.callback)
        self._init_widgets()

    def _init_widgets(self):
        self.label1 = Label(self.frame, text="Phone number")
        self.label1.grid(row=0, sticky=W)
        self.entry1 = Entry(self.frame)
        self.entry1.grid(row=1, column=0)

        self.label2 = Label(self.frame, text="Label")
        self.label2.grid(row=0, column=1, sticky=W)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=1, column=1)
        '''
        self.label1 = Label(self.frame, text="First Name")
        self.label1.grid(row=0, sticky=W)
        self.entry1 = Entry(self.frame)
        self.entry1.grid(row=1, column=0)

        self.label2 = Label(self.frame, text="Last Name")
        self.label2.grid(row=0, column=1, sticky=W)            self.entry1.get(), self.entry2.get(),
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=1, column=1)

        self.label3 = Label(self.frame, text="E-mail")
        self.label3.grid(row=2, sticky=W, columnspan=2)
        self.entry3 = Entry(self.frame)
        self.entry3.grid(row=3, sticky=W+E, columnspan=2)

        self.label4 = Label(self.frame, text="Label")
        self.label4.grid(row=3, sticky=E, columnspan=2)
        self.entry4 = Entry(self.frame)
        self.entry4.grid(row=4, sticky=E+W, columnspan=2)
        '''
        self.btn_ok = Button(self.frame, text="OK", width=7, command=self.btnok_click)
        self.btn_ok.grid(row=4, column=1, sticky=E)

    def btnok_click(self):
        items = (self.entry1.get(), self.entry2.get())
        if '' in items:
            print('please fill all boxes')
            return 'break'
        sql.session.insert_phone(items)

        self._okbtn_clicked = 1
        print('user exits the screen by clicking ok button')
        self.frame.destroy()

    def callback(self):

        self._okbtn_clicked = 0
        print('user exits the screen')
        self.frame.destroy()
