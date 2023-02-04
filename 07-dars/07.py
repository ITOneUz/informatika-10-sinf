from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Button bilan ishlash")

l = Label(root, text="ITONE.UZ", fg="red", bg="white", width="400")
l.pack()

def HellW():
	print("salom dunyo")

btn = Button(root, text="1-tugma", fg="red", bd=1, command=HellW)
btn.place(x=30, y=50)

btn2 = Button(root, text="2-tugma", fg="blue", bd=1, height="6", width="12")
btn2.place(x=30, y=80)

btn3 = Button(root, text="3-tugma", fg="yellow", bd=1, padx=20, pady=20)
btn3.place(x=30, y=210)

root.mainloop()