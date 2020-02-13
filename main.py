import os



def create_files():
    cwd = "C:\Semester"
    standar = ["index.html","style.css","script.js"]

    def create_dir(folder):
    	try:
    		if not os.path.exists(folder):
    			os.mkdir(folder)
    	except OSError:
    		print("Folder exist")


    def standar_project():
    	os.chdir(cwd)
    	create_dir("Home")
    	standar = ["index.html","style.css","script.js"]
    	#for x in standar:f = open(f"{x}", "w")
    standar_project()
    

    def python_project():
    	standar.append("hello.py")
    	for x in standar:f = open(f"{x}","w")

