from tkinter import *
from tkinter.ttk import *
from GUIPeople import People
from GUIEmail import Email
from GUIAddress import Address
from GUIPhone import PhoneNumber
#from importGUI import importForm
#from exportGUI import exportForm

def label_entry(frmlblent, txtlbl, txtlbl2=None):
    label = Label(frmlblent, text=txtlbl)
    label.pack(side=LEFT)
    frmlblent._entry = Entry(frmlblent)
    frmlblent._entry.pack(side=LEFT)

    if txtlbl2:
        label2 = Label(frmlblent, text=txtlbl2)
        label2.pack(side=LEFT)
        frmlblent._entry2 = Entry(frmlblent)
        frmlblent._entry2.pack(side=LEFT)


class FormMenu:
    """This is the main form that shows after user login.
    Contains
    =========
    --> Label shows login Company name.
    --> Three Buttons
        --> people:   OnClick Shows Formpeople,
        --> Invoices:   OnClick Shows FormInvoices,
        --> Customers:  OnClick shows FormCustomers
    --> A background Image
    """
    def __init__(self, master):
        self.master = master
        self.frm_invoices = None

    def _init_widgets(self):
        self.buttons = Frame(self.master)
        Label(self.buttons, text='Welcome! Please select one option from the choices below').pack(side=TOP)
        # People button
        self.peoplebtn = Button(self.buttons, text="People", command=self.peopleClick)
        self.peoplebtn.pack(side='top')
        # Phone number button
        self.phonebtn = Button(self.buttons, text="Phone Number", command=self.phone_click)
        self.phonebtn.pack(side='top')
        #Email button
        self.embtn = Button(self.buttons, text="Email", command=self.email_click)
        self.embtn.pack(side='top')
        #Address button
        self.addbtn = Button(self.buttons, text="Addresses", command=self.addClick)
        self.addbtn.pack(side='top')
        # button invoices
        self.importbtn = Button(self.buttons, text='Import', command=self.imClick)
        self.importbtn.pack(side='top')
        # button customers
        self.exportbtn = Button(self.buttons, text='Export', command=self.exClick)
        self.exportbtn.pack(side='top')

        self.printbtn = Button(self.buttons, text='Print Mailing Label', command=self.printClick)
        self.printbtn.pack(side='top')
        self.buttons.pack(side='bottom',padx=10)

    def peopleClick(self):
        print("people!!!")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.phonebtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
        self.frm_people = People()
        self.master.wait_window(self.frm_people.frame)
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.phonebtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL

    def email_click(self):
        print("email")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.phonebtn['state'] = DISABLED
        self.addbtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
        self.frm_email = Email()
        self.master.wait_window(self.frm_email.frame)
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.phonebtn['state'] = DISABLED
        self.addbtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL

    def phone_click(self):
        print("phone")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.phonebtn['state'] = DISABLED
        self.addbtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
        self.frm_phone = PhoneNumber()
        self.master.wait_window(self.frm_phone.frame)
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.phonebtn['state'] = NORMAL
        self.addbtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL

    def addClick(self):
        print("addresses")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.addbtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
        self.frm_address = Address()
        self.master.wait_window(self.frm_address.frame)
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.addbtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL

    def imClick(self):
        print ("import")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.addbtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
        #self.frm_import=importForm() #IMPORT CLASS INIT HERE
        self.master.wait_window(self.frm_import.frame)
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.addbtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL

    def exClick(self):
        print("export")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.addbtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
       # self.frm_export=exportForm()     #EXPORT CLASS INIT HERE
        self.master.wait_window(self.frm_export.frame)
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.addbtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL

    def printClick(self):
        print("print mailing label")
        self.peoplebtn['state'] = DISABLED
        self.embtn['state'] = DISABLED
        self.addbtn['state'] = DISABLED
        self.importbtn['state'] = DISABLED
        self.exportbtn['state'] = DISABLED
        self.peoplebtn['state'] = DISABLED
        self.printbtn['state'] = DISABLED
      #  self.frm_print=Print()     #PRINT CLASS INIT HERE
        self.master.wait_window(self.frm_print.frame)
        self.peoplebtn['state'] = NORMAL
        self.peoplebtn['state'] = NORMAL
        self.embtn['state'] = NORMAL
        self.addbtn['state'] = NORMAL
        self.importbtn['state'] = NORMAL
        self.exportbtn['state'] = NORMAL
        self.printbtn['state'] = NORMAL