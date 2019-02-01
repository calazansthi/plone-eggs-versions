import os
 
path = '.'
items = sorted(os.listdir(path))

with open("versions.cfg", "w") as file: 
    file.write("[versions]\n")        
    
    for name in items:
        if ((name == "eggs.py") or (name == "versions.cfg")):
            pass
        else:
            nameList = name.split('-')
            product = nameList[0]
            version = nameList[1]

            file.write(product + " = " + version + "\n")                    

            print(product + " = " + version)