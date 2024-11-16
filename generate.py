import os
from pathlib import Path
files = []
for x in os.walk("assets\\chill\\textures\\icons\\class"):
    if x[2]:
        for file in x[2]:
            path = str(x[0])+str(file)
            path = path.replace("assets\\chill\\textures\\icons\\", "")
            path = path.replace(file, "")

            files.append([path, file])
print(files)
for file in files:
    try:
        os.makedirs(file[0])
    except:
        print("failed to create directory")
    f = open(file[0] + "\\" + Path(file[1]).stem + ".json", "w")
    f.write("""{
    "parent": "minecraft:item/handheld",
    "textures": {
        "layer0": "chill:icons/""" + file[0].replace("\\", "/") + "/" + Path(file[1]).stem + """"
    }
}""")
    f.close()
