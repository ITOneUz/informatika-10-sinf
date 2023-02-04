from tkinter import *

window = Tk()
window.geometry('400x300')
window.title('14-dars - itone.uz')
window.config(pady=20, padx=20)

lb = LabelFrame(window, text="Bu labelframe")
lb.pack(fill="both", expand="yes")

Label(lb, text="itone.uz").pack()

def new_win():
	new = Toplevel(window)
	new.geometry("300x200")
	new.title("About Form")
	Label(new, text="Bu malumot dastur xaqida", font=('Consolas 14 bold')).pack()

Button(window, text="Dastur xaqida", command=new_win).pack()

window.mainloop()
