from tkinter import *
from functools import partial

window = Tk()  
window.geometry('400x150')  
window.title('Entry va Grid bilan ishlash')

def VLogin(username, password):
	print("username:", username.get())
	print("password:", password.get())

	if (username.get() == "admin" and password.get() == "admin"):
		print("Hush kelibsiz")

username = StringVar()
enLoginLabel = Label(window, text="Login").grid(row=0, column=0)
enLogin = Entry(window, textvariable=username).grid(row=0, column=1)

password = StringVar()
enPasLabel = Label(window, text="Password").grid(row=1, column=0)
enPassword = Entry(window, textvariable=password, show='*').grid(row=1, column=1)

VLogin = partial(VLogin, username, password)

lbtn = Button(window, text="Login", command=VLogin).grid(row=2, column=1)

window.mainloop()