# # # # # # # # # # # # #
# Coder: KP
# Hμερ: 29/07/2020
# Last Update: 30/07/2020
# # # # # # # # # # # # #

from tkinter import *

def action():
    root = Tk()

    root.title("Menu")
    root.geometry("700x300+500+250")

    img_write = PhotoImage( file = 'Eikones\\write.gif' )
    L_img_write = Button( root, image = img_write )
    L_img_write.place(x=10,y=20)   
    L_write = Label(root, text='Write new entry',font=('Constantia',14)).place(x=90,y=40)

    img_edit = PhotoImage( file = 'Eikones\\edit-entry.gif' )  
    L_img_edit = Button( root, image = img_edit )
    L_img_edit.place(x=10,y=105)
    L_edit = Label(root, text='Edit entry',font=('Constantia',14)).place(x=90,y=125)

    img_del_entry = PhotoImage( file = 'Eikones\\delete-entry.gif' )
    L_img_del_entry = Button( root, image = img_del_entry )
    L_img_del_entry.place(x=10,y=190)
    L_del_entry = Label(root, text='Delete entry',font=('Constantia',14)).place(x=90,y=210)

    img_new_bk = PhotoImage( file = 'Eikones\\New-book.gif' )
    L_img_new_bk = Button( root, image = img_new_bk )
    L_img_new_bk.place(x=350,y=20)   
    L_new_bk = Label(root, text='Create new book',font=('Constantia',14)).place(x=430,y=40) 

    img_del_bk = PhotoImage( file = 'Eikones\\delete-book.gif' )
    L_img_del_bk = Button( root, image = img_del_bk )
    L_img_del_bk.place(x=350,y=105)
    L_delete_bk = Label(root, text='Delete book',font=('Constantia',14)).place(x=430,y=125) 

    img_shelf = PhotoImage( file = 'Eikones\\book-shelf.gif' )
    L_img_shelf = Button( root, image = img_shelf )
    L_img_shelf.place(x=350,y=190) 
    L_bk_shelf = Label(root, text='Book Shelf',font=('Constantia',14)).place(x=430,y=210) 

    root.mainloop()

if __name__=='__main__':
    action()