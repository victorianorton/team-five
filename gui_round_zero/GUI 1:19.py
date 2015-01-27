__author__ = 'Kpinto'

from Tkinter import *
from Tkinter import Frame, Tk, BOTH, Text, Menu, END
from ttk import Frame, Button, Label, Style
from ttk import Entry
import tkFileDialog


class dialPad(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Dial Pad")

        Style().configure("TButton", padding=(0, 5, 0, 5),
                          font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=3, sticky=W + E)
        nine = Button(self, text="9")
        nine.grid(row=1, column=0)
        #OnClick()
        eight = Button(self, text="8")
        eight.grid(row=1, column=1)
        #OnClick()

        seven = Button(self, text="7")
        seven.grid(row=1, column=2)
        #OnClick()

        six = Button(self, text="6")
        six.grid(row=2, column=0)
        #OnClick()

        five = Button(self, text="5")
        five.grid(row=2, column=1)
        #OnClick()

        four = Button(self, text="4")
        four.grid(row=2, column=2)
        #OnClick()

        three = Button(self, text="3")
        three.grid(row=3, column=0)
        #OnClick()

        two = Button(self, text="2")
        two.grid(row=3, column=1)
        #OnClick()

        one = Button(self, text="1")
        one.grid(row=3, column=2)
        #OnClick()

        pound = Button(self, text="#")
        pound.grid(row=4, column=0)
        #OnClick()

        zero = Button(self, text="0")
        zero.grid(row=4, column=1)
        #OnClick()

        star = Button(self, text="*")
        star.grid(row=4, column=2)
        #OnClick()

        self.pack()

        # def OnClick(self):


class openDB(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [('Address database', '.db'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text


class mainWin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

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

        addVar = IntVar()
        searchVar = IntVar()
        sortVar = IntVar()
        groupVar = IntVar()
        favVar = IntVar()
        dialVar = IntVar()
        printVar = IntVar()
        impVar = IntVar()
        expVar = IntVar()
        mergeVar = IntVar()

        mb.menu.add_checkbutton(label="New Contact",
                                variable=addVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Search",
                                variable=searchVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Sort",
                                variable=sortVar)
        #OnClick()
        mb.menu.add_checkbutton(label="Groups",
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
        #OnClick()

        # mb.pack() --- DO NOT UNCOMMENT THIS. IT WILL BREAK THE CODE


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

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        #Trying to add in text before entry boxes...it's having some issues right now.
        #nText = Text(self)
        #nText.insert(END, "Name: ")
        #nText.wrap=WORD
        #nText.grid(row=0, column=0)

        #Text boxes for entering name, address, phone, and email
        nEntry = Entry(self)
        nEntry.grid(row=0, column=0, columnspan=2, sticky=W + E)

        aEntry1 = Entry(self)
        aEntry1.grid(row=0, column=2, columnspan=2, sticky=W+E)

        p1Entry = Entry(self)
        p1Entry.grid(row=1, column=0, columnspan=2, sticky=W+E)

        eEntry = Entry(self)
        eEntry.grid(row=1, column=2, columnspan=2, sticky=W+E)

        #paEntry = Entry(self)
        #paEntry.grid(row=1, column=4, columnspan=2, sticky=W+E)

        self.pack()



def main():
    root = Tk()  #main UI window root
    #root.geometry("300x250+300+300")
    #root1 = Tk()
    #imdb = openDB(root) -- #open file dialogue
    #app = dialPad(root1) - #dialpad
    #sear = search(root) #search popup
    #sor = sort(root) #sort popup
    #wind = mainWin(root) #Main window
    newc = newContact(root) #new contact
    root.mainloop() #Init root
    #root1.mainloop()


if __name__ == '__main__':
    main()