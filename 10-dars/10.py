from tkinter import *

window = Tk()  
# window.geometry('300x200')
window.title('10-dars')

frame = Frame(window)
frame.pack(side=LEFT)

frame2 = Frame(window)
frame2.pack(side=RIGHT)

b1 = Button(frame, text="1-tugma")
b1.pack(side=LEFT)

b2 = Button(frame, text="2-tugma")
b2.pack(side=LEFT)

b3 = Button(frame2, text="3-tugma")
b3.pack(side=TOP)

b4 = Button(frame2, text="4-tugma")
b4.pack(side=TOP)

b5 = Button(frame2, text="5-tugma")
b5.pack(side=TOP)

window.mainloop()