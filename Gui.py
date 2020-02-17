import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkfilebrowser import askopendirname 




class File_Gui(tk.Tk):
    
	def __init__(self,StringVar):
		tk.Tk.__init__(self)
		self.title = "File Generator"
		self.geometry("400x200")
		self.resizable(False,False)
		self.button = ttk.Button(self,text="Browse",command=self.searc_button).pack()
		self.StringVar = StringVar
		self.combo = ttk.Combobox(self,textvariable = self.StringVar,values=["Standard", "Bootstrap", "SASS"]).pack()	
		self.name_entry = ttk.Entry(self).pack()
		self.buttonTwo = ttk.Button(self,text="Create Folder", command = self.create_folder).pack()


	def create_folder(self):
		pass


		

	def searc_button(self):

		
		



if __name__ == "__main__":
	Gui = File_Gui("StringVar")
	Gui.mainloop()

