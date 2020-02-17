import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os 


class File_Gui(tk.Tk):
    
	def __init__(self):
		tk.Tk.__init__(self)
		self.title = "File Generator"
		self.geometry("400x200")
		self.resizable(False,False)
		self.StringVar = tk.StringVar()
		self.combo = ttk.Combobox(self,textvariable = self.StringVar,values=["Standard", "Bootstrap", "SASS"]).pack()	
		self.name_entry = ttk.Entry(self).pack()
		self.buttonTwo = ttk.Button(self,text="Create Folder", command = self.create_folder).pack()

		

	def create_folder(self):
		self.filename = filedialog.askdirectory()
		

		try:
			self.find = os.chdir(self.filename)
			self.createFolder = os.mkdir("Project")
			self.openFolder = os.startfile(f"{self.filename}\\Project")
		
		except:
			self.errormes = messagebox.showerror("Error", "The are an existing folder")
		
	


if __name__ == "__main__":	

	Gui = File_Gui()
	Gui.mainloop()


