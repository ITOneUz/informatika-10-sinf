from tkinter import *
import webbrowser

window = Tk()  
window.geometry('500x400')
window.title('project - itone.uz')

def new_win():
	new = Toplevel(window)
	new.geometry("300x200")
	new.title("About Form")
	Label(new, text="Bu malumot dastur xaqida", font=('Consolas 14 bold')).pack(pady=20)

def web_page():
	url = "https://www.itone.uz"
	webbrowser.open_new(url)

asosiymenu = Menu(window)
window.config(menu=asosiymenu)

filemenu = Menu(asosiymenu, tearoff=0)
helpmenu = Menu(asosiymenu, tearoff=0)

filemenu.add_command(label="Open...")
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu.add_command(label="Help", command=web_page)
helpmenu.add_command(label="About me", command=new_win)

asosiymenu.add_cascade(label="File", menu=filemenu)
asosiymenu.add_cascade(label="Aditional", menu=helpmenu)

window.mainloop()
