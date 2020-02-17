import os
from tkfilebrowser import askopendirname 

ecoh = ""


	


def create_files():    
    standar = ["index.html","style.css","script.js"]

    def create_dir(folder):
    	try:
    		if not os.path.exists(folder):
    			os.mkdir(folder)
    	except OSError:
    		print("Folder exist")

	


    def standar_project(): 
    	folder = askopendirname(title="Choose your directory")
    	os.chdir(folder)
    	create_dir("Home")
    	standar = ["index.html","style.css","script.js"]
    	#for x in standar:f = open(f"{x}", "w")
    standar_project()
    
