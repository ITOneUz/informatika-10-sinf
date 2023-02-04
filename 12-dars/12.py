from tkinter import *
from tkinter import messagebox

window = Tk()  
window.geometry('400x300')
window.title('12-dars - itone.uz')
window.config(pady=20, padx=20)

var = IntVar()

def sel():
	if(var.get() == 1):
		btn.config(state="normal")
	else:
		btn.config(state="disabled")

label = Label(window, text="Kompaniya shartlariga rozimisiz?")
label.pack(anchor=W)

Radiobutton(window, text="Roziman", variable=var, value=1, command=sel).pack(anchor=W)
Radiobutton(window, text="Rozi emasman", variable=var, value=0, command=sel).pack(anchor=W)

btn = Button(window, text="Kirish", state="disabled", command=lambda: messagebox.showinfo("sarlavha", "Hush kelibsiz"))
btn.pack(anchor=W)

window.mainloop()
