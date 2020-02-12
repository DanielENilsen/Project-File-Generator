from tkinter import*
from tkinter import ttk
from tkinter import filedialog


def file_dialog(event):
	root.filename = filedialog.askopenfilename()



root = Tk()

root.geometry("400x200")
root.resizable(False,False)

btn = ttk.Button(root, text= "Choose Folder")
btn.bind("<Button-1>",file_dialog)
btn.pack()


String_var = StringVar()
Select_projects = ttk.Combobox(root, textvariable = String_var,values=["Standard", "Bootstrap", "SASS"]).pack()

root.mainloop()