
from Tkinter import *
from Tkinter import Frame, Tk, BOTH, Text, Menu, END
from ttk import Frame, Button, Label, Style
from ttk import Entry
import tkFileDialog
import csv
import os
import shutil

#This is skeleton stuff. This class can pretty much be ignored.
class openDB(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("File dialog")
        #self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        file = tkFileDialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        if file != None:
            data = file.read()
        #fl = read.show()

        #if fl != '':
        #    text = self.readFile(fl)
        #   self.txt.insert(END, text)

    #def readFile(self, filename):
    #    f = open(filename, "r")
     #   text = f.read()
      #  return text


class mainWin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        NC = False
        SC = False
        ST = False
        if NC == True:
            self.initNC()
        if SC == True:
            self.initSC()
        if ST == True:
            self.initST()


    def initUI(self):
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
        '''
        addPerson = Button(self, text="New Contact")
        addPerson.grid(row=0, column=0)

        name = Button(self, text="Name")
        name.grid(row=0, column=1)

        priPhone = Button(self, text="Primary Phone")
        priPhone.grid(row=0, column=2)

        priEmail = Button(self, text="Primary Email")
        priEmail.grid(row=0, column=3)

        priAdd = Button(self, text="Primary Address")
        priAdd.grid(row=0, column=4)

        search = Button(self, text="Search")
        search.grid(row=1, column=0)

        sort = Button(self, text="Sort")
        sort.grid(row=2, column=0)

        groups = Button(self, text="Group")
        groups.grid(row=3, column=0)

        favorites = Button(self, text="Favorites")
        favorites.grid(row=4, column=0)

        mailLabel = Button(self, text="Print")
        mailLabel.grid(row=5, column=0)

        dialPad = Button(self, text="Dial Pad")
        dialPad.grid(row=6, column=0)

        importBook = Button(self, text="Import")
        importBook.grid(row=7, column=0)

        exportBook = Button(self, text="Export")
        exportBook.grid(row=8, column=0)

        merge = Button(self, text="Merge")
        merge.grid(row=9, column=0)

        self.pack()
        '''

        ##Here's where the problem starts. It's basically you can have buttons or menus.
        ##Having both causes the program to stall out

        ##EDIT: The issue is fixed!

        name = Button(self, text="Name")
        name.grid(row=0, column=1)
        #OnClick() -- a quick way to sort alphabetically?
        priPhone = Button(self, text="Primary Phone")
        priPhone.grid(row=0, column=2)
        #OnClick() -- a quick way to sort by the primary phone
        priEmail = Button(self, text="Primary Email")
        priEmail.grid(row=0, column=3)
        #OnClick() -- a quick way to sort by the primary phone
        priAdd = Button(self, text="Primary Address")
        priAdd.grid(row=0, column=4)
        #Onclick() -- a quick way to sort by primary address
        self.pack()

        ##The drop down menu starts here!
        mb = Menubutton(self, text="Options", relief=RAISED)
        mb.grid(row=0, column=0)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        '''addVar = IntVar()
        searchVar = IntVar()
        sortVar = IntVar()
        groupVar = IntVar()
        favVar = IntVar()
        dialVar = IntVar()
        printVar = IntVar()
        impVar = IntVar()
        expVar = IntVar()
        mergeVar = IntVar()
        '''

        mb.menu.add_command(label="New Contact", command=self.onNC)#once more)
        #command=self.onClick()
        mb.menu.add_checkbutton(label="Search",
                                command=self.onSC)
        #OnClick()
        mb.menu.add_checkbutton(label="Sort",
                                command=self.onST)
        #OnClick()
        '''mb.menu.add_checkbutton(label="Groups",
                                variable=groupVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Favorites",
                                variable=favVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Dial Pad",
                                variable=dialVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Print",
                                variable=printVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Merge",
                                variable=mergeVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Import",
                                variable=impVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Export",
                                variable=expVar)
        #OnClick()'''

        # mb.pack() --- DO NOT UNCOMMENT THIS. IT WILL BREAK THE CODE
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
        NC = True
        self.initNC()

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

        #Text boxes for entering name, address, phone, and email
        self.instruction = Label(self, text="Enter Name:")
        self.instruction.grid(row=1, column=0,sticky=W)
        nEntry = Entry(self)
        nEntry.grid(row=1,column=1, columnspan=2)

        self.instruction = Label(self, text="Enter Address:")
        self.instruction.grid(row=1, column=3)
        aEntry1 = Entry(self)
        aEntry1.grid(row=1, column=4, columnspan=2)

        self.instruction = Label(self, text="Enter Phone:")
        self.instruction.grid(row=2, column=0,sticky=W)
        p1Entry = Entry(self)
        p1Entry.grid(row=2, column=1, columnspan=2)

        self.instruction = Label(self, text="Enter Email:")
        self.instruction.grid(row=2, column=3)
        eEntry = Entry(self)
        eEntry.grid(row=2, column=4, columnspan=2)

        plusP = Button(self, text="+Phone")
        plusP.grid(row=2, column=6)
        #OnClick()
        plusA = Button(self, text="+Address")
        plusA.grid(row=1, column=6)
        #OnClick()
        plusE = Button(self, text="+Email")
        plusE.grid(row=1, column=7)
        #OnClick()
        conf = Button(self, text="Confirm")
        conf.grid(row=2, column=7)
        #OnClick()

        self.pack()

    def initST(self):
        self.parent.title("Sort by:")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        sName = Button(self, text="Name")
        sName.grid(row=0, column=0)
        #OnClick()

        sAdd = Button(self, text="Address")
        sAdd.grid(row=0, column=1)
        #OnClick()

        sZip = Button(self, text="ZIP")
        sZip.grid(row=0, column=2)
        #OnClick()

        sPh = Button(self, text="Phone")
        sPh.grid(row=1, column=0)
        #OnClick()

        sEm = Button(self, text="Email")
        sEm.grid(row=1, column =1)
        #OnClick()

        sGr = Button(self, text="Groups")
        sGr.grid(row=1, column=2)
        #OnClick()

        self.pack()


class search(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
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


class sort(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Sort by:")
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        sName = Button(self, text="Name")
        sName.grid(row=0, column=0)
        #OnClick()

        sAdd = Button(self, text="Address")
        sAdd.grid(row=0, column=1)
        #OnClick()

        sZip = Button(self, text="ZIP")
        sZip.grid(row=0, column=2)
        #OnClick()

        sPh = Button(self, text="Phone")
        sPh.grid(row=1, column=0)
        #OnClick()

        sEm = Button(self, text="Email")
        sEm.grid(row=1, column =1)
        #OnClick()

        sGr = Button(self, text="Groups")
        sGr.grid(row=1, column=2)
        #OnClick()

        self.pack()


class newContact(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
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

        #Text boxes for entering name, address, phone, and email
        self.instruction = Label(self, text="Enter Name:")
        self.instruction.grid(row=0, column=0,sticky=W)
        nEntry = Entry(self)
        nEntry.grid(row=0,column=1, columnspan=2)

        self.instruction = Label(self, text="Enter Address:")
        self.instruction.grid(row=0, column=3)
        aEntry1 = Entry(self)
        aEntry1.grid(row=0, column=4, columnspan=2)

        self.instruction = Label(self, text="Enter Phone:")
        self.instruction.grid(row=1, column=0,sticky=W)
        p1Entry = Entry(self)
        p1Entry.grid(row=1, column=1, columnspan=2)

        self.instruction = Label(self, text="Enter Email:")
        self.instruction.grid(row=1, column=3)
        eEntry = Entry(self)
        eEntry.grid(row=1, column=4, columnspan=2)

        plusP = Button(self, text="+Phone")
        plusP.grid(row=1, column=6)
        #OnClick()
        plusA = Button(self, text="+Address")
        plusA.grid(row=0, column=6)
        #OnClick()
        plusE = Button(self, text="+Email")
        plusE.grid(row=0, column=7)
        #OnClick()

        conf = Button(self, text="Confirm")
        conf.grid(row=1, column=8)
        #OnClick()

        self.pack()

class viewCon(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
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
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)

        self.instruction = Label(self, text="Contact Name", relief=GROOVE)
        self.instruction.grid(row=0, column=0, sticky=W)

        self.instruction = Label(self, text="Address(es)", relief=GROOVE)
        self.instruction.grid(row=0, column=2)

        self.instruction = Label(self, text="Insert Picture")
        self.instruction.grid(row=1, column=0, rowspan=2, columnspan=2)

        self.instruction = Label(self, text="phone(s)", relief=GROOVE)
        self.instruction.grid(row=0, column=3)

        self.instruction = Label(self, text="email(s)", relief=GROOVE)
        self.instruction.grid(row=0, column=4)

        edit = Button(self, text="Edit")
        edit.grid(row=3, column=0)

        remo = Button(self, text="Remove")
        remo.grid(row=3, column=1)

        group = Button(self, text="Group")
        group.grid(row=4, column=0)

        self.pack()


def main():
    root = Tk()  #main UI window root
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
    st = False
    if st == True:
        newc = newContact(root) #new contact
    #viewc = viewCon(root6) #view contact
    root.mainloop() #Init root
    #root1.mainloop()


if __name__ == '__main__':
    main()