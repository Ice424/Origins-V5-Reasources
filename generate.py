import os
from pathlib import Path
files = []
predicates = []
model_num = 4
for x in os.walk("assets\\chill\\textures\\item\\icons\\class"):
    if x[2]:
        for file in x[2]:
            path = str(x[0])+str(file)
            path = path.replace("assets\\chill\\textures\\item\\icons\\", "")
            path = path.replace(file, "")

            files.append([path, file])
print(files)
for file in files:
    try:
        os.makedirs(file[0])
    except:
        print("failed to create directory")
        
    predicates.append('{"predicate": {"custom_model_data": '+ str(model_num) +' }, "model":"chill:item/custom/icons/' +file[0] + "\\" + Path(file[1]).stem + '"},')
    model_num += 1
    f = open(file[0] + "\\" + Path(file[1]).stem + ".json", "w")
    f.write("""{
    "parent": "minecraft:item/handheld",
    "textures": {
        "layer0": "chill:item/icons/""" + file[0].replace("\\", "/") + "/" + Path(file[1]).stem + """"
    }
}""")
    f.close()
for predicate in predicates:
    print(predicate.replace("\\", "/"))
