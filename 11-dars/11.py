from tkinter import *

window = Tk()  
window.geometry('400x300')
window.title('11-dars - itone.uz')

asosiymenu = Menu(window)
window.config(menu=asosiymenu)

filemenu = Menu(asosiymenu, tearoff=0)
helpmenu = Menu(asosiymenu, tearoff=0)

filemenu.add_command(label="Open...")
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu.add_command(label="Help")
helpmenu.add_command(label="About me")

asosiymenu.add_cascade(label="File", menu=filemenu)
asosiymenu.add_cascade(label="Aditional", menu=helpmenu)

window.mainloop()
