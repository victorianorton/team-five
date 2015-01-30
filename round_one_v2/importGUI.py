__author__ = 'Kpinto'
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
import csv
import shutil



class importForm:
    def __init__(self):
        #self.frame = Toplevel()
        self.import_tsv()

    def import_tsv(self):
        try:
            file = filedialog.askopenfilename(filetypes=[('Tab separated values', '*.tsv')],
                                       title='Choose a file to import')

            pwd = os.path.join(file)

            print(pwd)
            abs_path = os.path.abspath(file)
            print(abs_path)
            mv = shutil.copy(abs_path, os.getcwd())
            r_csv = csv.reader(open(abs_path, "rb"))
            fhand = open(abs_path)
        except:
            print('File cannot be opened: ')#, file)
            exit()
