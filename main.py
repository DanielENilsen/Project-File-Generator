import os





def create_files():
    cwd = os.getcwd()
    standar = ["index.html","style.css","script.js"]


    def standar_project():
    	standar = ["index.html","style.css","script.js"]
    	for x in standar:f = open(f"{x}", "w")
    

    def python_project():
    	standar.append("hello.py")
    	for x in standar:f = open(f"{x}","w")


    #standar_project()
    python_project()


    	




create_files()

