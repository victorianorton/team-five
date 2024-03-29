#tb.py

from tkinter import *
def _init_toolbar(tbmaster):
    
    '''TOOLBAR CONTAINS ADD, EDIT, DELETE AND FIND BUTTONS
        the argment is a class and it must have:
        tbmaster.frame              :- a root window class
        tbmaster.btn_add_click()    :- a method
        tbmaster.btn_edit_click()
        tbmaster.btn_delete_click()
        tbmaster.btn_find_click()
        '''
    tbmaster.tb=Frame(tbmaster.frame,borderwidth=1)#,relief=)
    tbmaster.tb.pack(side=TOP,fill=X)#####
    
    tbmaster.btn_add=Button(tbmaster.tb,command=tbmaster.btn_add_click)
    tbmaster.imgadd=PhotoImage(file="img/add.gif")
    tbmaster.btn_add['image']=tbmaster.imgadd
    tbmaster.btn_add.pack(side=LEFT,padx=4,pady=4)
    
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
    tbmaster.entryfind.pack(side=LEFT,padx=4,pady=4)

