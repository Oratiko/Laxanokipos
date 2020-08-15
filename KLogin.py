# # # # # # # # # # # # #
# Coder: KP
# Hμερ: 28/07/2020
# Last Update: 30/07/2020
# # # # # # # # # # # # #

import hashlib
from tkinter import *
import json
import time

root = Tk()
root.title('Login')
root.geometry('370x160+500+250')   # to + einai pou na anixi stin othoni(x,y)

Luser = Label(root, text='Username', font=('Constantia',12)).place(x=50,y=40)
Lpasswd = Label(root, text='Password', font=('Constantia',12)).place(x=50,y=60)

username = StringVar()
passwd = StringVar()

Euser = Entry(root, textvariable = username, width=30).place(x=125,y=40)
Epasswd = Entry(root, textvariable = passwd, show='*', width=30).place(x=125, y=60)

global flag, counter

def CheckLogin():
	global flag, counter
	user = str(username.get())
	kodikos = str(passwd.get())
	kodikos = hashlib.sha256(kodikos.encode()).hexdigest() 
	with open('config.json','r') as f:
		line = json.load(f)
	if kodikos == str(line['password']):
		flag = True
		root.destroy()
	else:
		flag = False
		error = Label(root, text='Wrong Passcode !!!',fg='red').place(x=130,y=110)
		counter +=1
		if counter > 2:
			error = Label(root, text='App Exiting...Due to continues wrong passcodes!!!',fg='red').place(x=70,y=110)
			root.after(5000,root.destroy)
			flag = False
			
		
flag, counter = None, 0

sub = Button(root, text='Submit', command=CheckLogin).place(x=165,y=80)

root.mainloop()


