from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x300")
window.title("CHECKBOX")

l = Label(window, text="Nothing:)")
l.pack()

def myFunc():
	# print(var1.get())

	if (var1.get() == 1):
		# l.config(text="Siz keyingi bosqichga o'tdingiz:)")
		l["text"]="Keyingi bosqichga otishingiz mumkin:)"
		b["state"] = "normal"

	if (var1.get() == 0):
		l.config(text="Siz keyingi bosqichga o'tmadingiz")
		b["state"] = "disabled"

def myFunc2():
	messagebox.showinfo("sarlavha", "Hush kelibsiz!")

var1 = IntVar()

c = Checkbutton(window, text="Kompaniya shartlariga roziman!", variable=var1, onvalue=1, offvalue=0, command=myFunc)
c.pack()

b = Button(window, text="Kirish", state="disabled", command=myFunc2)
b.pack()

b2 = Button(window, text="Chiqish", command=window.quit)
b2.pack()

window.mainloop()