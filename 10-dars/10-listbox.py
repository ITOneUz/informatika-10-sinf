from tkinter import *

window = Tk()  
window.geometry('350x250')
window.title('10-dars')

frame = Frame(window)
frame.pack(side=LEFT, padx=20)

frame2 = Frame(window)
frame2.pack(side=RIGHT, padx=20)

def Add():
	lb1.insert(0, language.get())
	en1.delete(0, END)

def Delete():
	select = lb1.curselection()
	lb1.delete(select[0])

l1 = Label(frame, text="Dasturlash tilini kiriting:")
l1.pack()

language = StringVar()
en1 = Entry(frame, textvariable=language)
en1.pack()

b1 = Button(frame, text="Qo'shish", command=Add)
b1.pack(pady=5)

#listbox
lb1 = Listbox(frame2, width="20", height="10")
lb1.pack()

b5 = Button(frame2, text="O'chirish", command=Delete)
b5.pack(side=RIGHT)

window.mainloop()