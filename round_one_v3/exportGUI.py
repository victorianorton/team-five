__author__ = 'Kpinto'
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
import csv
import shutil

class exportForm:
    def __init__(self):
        #self.frame = Toplevel()
        self.export_tsv()

    def export_tsv(self):
        try:
            file = filedialog.asksaveasfilename(defaultextension=".tsv")
            pwd = os.path.join(file)
            print(pwd)
            print(os.getcwd())
            w_csv = csv.writer(open(pwd, "wb"))
            with open(pwd, "wb") as output:
                output.write()
                ## WE NEED TO INTEGRATE THIS
        except:
            print('File cannot be saved: ')
            exit()