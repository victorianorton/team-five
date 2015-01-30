__author__ = 'Victoria'

from tkinter import *


def _init_toolbar(tbmaster):

    tbmaster.tb = Frame(tbmaster.frame, borderwidth=1)
    tbmaster.tb.pack(side=TOP, fill=X)
    
    tbmaster.btn_insert_click = Button(tbmaster.tb, command=tbmaster.btn_insert_click)
    tbmaster.img_insert = PhotoImage(file="img/add.gif")
    tbmaster.btn_insert_click['image'] = tbmaster.img_insert
    tbmaster.btn_insert_click.pack(side=LEFT ,padx=4, pady=4)
    
    tbmaster.btn_edit=Button(tbmaster.tb,command=tbmaster.btn_edit_click)
    tbmaster.imgedit=PhotoImage(file="img/edit.gif")
    tbmaster.btn_edit['image']=tbmaster.imgedit
    tbmaster.btn_edit.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.btn_delete=Button(tbmaster.tb,command=tbmaster.btn_del_click)
    tbmaster.imgdel=PhotoImage(file="img/delete.gif")
    tbmaster.btn_delete['image']=tbmaster.imgdel
    tbmaster.btn_delete.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.btn_search=Button(tbmaster.tb,command=tbmaster.btn_search_click)
    tbmaster.imgsearch = PhotoImage(file="img/find.gif")
    tbmaster.btn_search['image'] = tbmaster.imgsearch
    tbmaster.btn_search.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.entryfind = Entry(tbmaster.tb)
    tbmaster.entryfind.pack(side=LEFT, padx=4, pady=4)

    tbmaster.btn_sort_name=Button(tbmaster.tb,command=tbmaster.btn_sort_name_click)
    tbmaster.imgsortname=PhotoImage(file="img/shop.gif")
    tbmaster.btn_sort_name['image']=tbmaster.imgsortname
    tbmaster.btn_sort_name.pack(side=LEFT,padx=4,pady=4)

def _init_sortbyzip(tbmaster):
    tbmaster.btn_sort_zip=Button(tbmaster.tb,command=tbmaster.btn_sort_zip_click)
    tbmaster.imgsortzip=PhotoImage(file="img/shop.gif")
    tbmaster.btn_sort_zip['image']=tbmaster.imgsortzip
    tbmaster.btn_sort_zip.pack(side=LEFT,padx=4,pady=4)