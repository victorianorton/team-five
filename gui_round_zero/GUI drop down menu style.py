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
        eight = Button(self, text="8")
        eight.grid(row=1, column=1)

        seven = Button(self, text="7")
        seven.grid(row=1, column=2)

        six = Button(self, text="6")
        six.grid(row=2, column=0)

        five = Button(self, text="5")
        five.grid(row=2, column=1)

        four = Button(self, text="4")
        four.grid(row=2, column=2)

        three = Button(self, text="3")
        three.grid(row=3, column=0)

        two = Button(self, text="2")
        two.grid(row=3, column=1)

        one = Button(self, text="3")
        one.grid(row=3, column=2)

        pound = Button(self, text="#")
        pound.grid(row=4, column=0)

        zero = Button(self, text="0")
        zero.grid(row=4, column=1)

        star = Button(self, text="*")
        star.grid(row=4, column=2)

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
        '''name.insert(INSERT, "Hello.....")
        name.insert(END, "Bye Bye.....")
        name.grid(row=0, column=1)
        '''
        self.pack()


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
        mb.menu.add_checkbutton(label="Search",
                                variable=searchVar)
        mb.menu.add_checkbutton(label="Sort",
                                variable=sortVar)
        mb.menu.add_checkbutton(label="Groups",
                                variable=groupVar)
        mb.menu.add_checkbutton(label="Favorites",
                                variable=favVar)
        mb.menu.add_checkbutton(label="Dial Pad",
                                variable=dialVar)
        mb.menu.add_checkbutton(label="Print",
                                variable=printVar)
        mb.menu.add_checkbutton(label="Merge",
                                variable=mergeVar)
        mb.menu.add_checkbutton(label="Import",
                                variable=impVar)
        mb.menu.add_checkbutton(label="Export",
                                variable=expVar)
       # mb.pack()


def main():
    root = Tk()
    # imdb = openDB(root)
    #root.geometry("300x250+300+300")
    #app = dialPad(root)
    wind = mainWin(root)
    root.mainloop()


if __name__ == '__main__':
    main()