import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class File_Gui(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title = "File Generator"
		self.geometry("400x200")
		self.button = ttk.Button(self,text="Browse",command=self.searc_button).pack()
		self.

	def searc_button(self):
		pass
		








if __name__ == "__main__":
	Gui = File_Gui()
	Gui.mainloop()

