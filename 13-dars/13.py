from tkinter import *

window = Tk()
window.geometry('400x300')
window.title('13-dars - itone.uz')
window.config(pady=20, padx=20)

var = IntVar()

def slider_sc(event):
	label.config(text=scale.get())

def sel():
	label.config(text=var.get())

scale = Scale(window, variable=var, from_=0, to=255, command=slider_sc, orient="horizontal")
scale.pack()

Button(window, text="natija", command=sel).pack()

label = Label(window)
label.pack()

var2 = IntVar()

def sbFunc():
	label2.config(text=var2.get())

sb = Spinbox(window, from_=0, to=200, textvariable=var2, command=sbFunc)
sb.pack()

label2 = Label(window)
label2.pack()

window.mainloop()
