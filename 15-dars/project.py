from tkinter import *
import webbrowser
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

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

# 15 dars

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(window, yscrollcommand=scrollbar.set)
text.insert(INSERT, "")
text.pack()

scrollbar.config(command=text.yview)

def OpenFile():
	global file
	file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
	if file == "":
		file = None
	else:
		window.title(os.path.basename(file) + " - Notepad")
		text.delete(1.0, END)
		f = open(file, "r")
		text.insert(1.0, f.read())
		f.close()

def newFile():
	global file
	window.title("Untitled - Notepad")
	file = None
	text.delete(1.0, END)

def SaveFile():
	global file
	if file == None:
		file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
		if file == "":
			file = None
		else:
			#Save as
			f = open(file, "w")
			f.write(text.get(1.0, END))
			f.close()

			window.title(os.path.basename(file) + " - Notepad")
			showinfo("Notepad", "File saved")
	else:
		# Save
		f = open(file, "w")
		f.write(text.get(1.0, END))
		f.close()

# 

filemenu = Menu(asosiymenu, tearoff=0)
helpmenu = Menu(asosiymenu, tearoff=0)

filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu.add_command(label="Help", command=web_page)
helpmenu.add_command(label="About me", command=new_win)

asosiymenu.add_cascade(label="File", menu=filemenu)
asosiymenu.add_cascade(label="Aditional", menu=helpmenu)

window.mainloop()
