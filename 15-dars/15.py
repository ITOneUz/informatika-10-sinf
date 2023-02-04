from tkinter import *

window = Tk()
window.geometry('500x400')
window.title('15-dars - itone.uz')
window.config(pady=20, padx=20)

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(window, yscrollcommand=scrollbar.set)
text.insert(INSERT, "malumot qo'shish")
text.insert(INSERT, "\n")
text.insert(END, "malumot qo'shish 2")
text.pack()

scrollbar.config(command=text.yview)

window.mainloop()
