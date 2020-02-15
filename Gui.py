from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from main import create_files,file_dialog




def submit_button():
	create_files()


def Gui_launch():
	root = Tk()
	root.geometry("400x200")
	root.resizable(False,False)

	btn = ttk.Button(root, text= "Choose Folder",command = file_dialog)	
	btn.pack()

	String_var = StringVar()
	Select_projects = ttk.Combobox(root, textvariable = String_var,values=["Standard", "Bootstrap", "SASS"]).pack()
	
	submit = ttk.Button(root,text = "Create Folder",command=submit_button)
	submit.place(x=150,y=80)

	name_entry = ttk.Entry(root)
	name_entry.place(x=120,y=100)

	root.mainloop()

if __name__ == "__main__":
	Gui_launch()