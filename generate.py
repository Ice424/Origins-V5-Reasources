import os
from pathlib import Path
os.chdir(Path(__file__).parents[2])
RESOURCES = os.path.abspath(
    ".\\resourcepacks\\Origins-V5-Reasources\\assets\\")
DATA = os.path.abspath(
    ".\\saves\\New World\\datapacks\\Origins-V5-Data\\data\\chill\\powers")

print(DATA)
#
powers = {
    "high": [],
    "low": [],
    "class": {
        "cleric": {
            "special": [],
            "high": [],
            "passive": []
        },
        "druid": {
            "special": [],
            "high": [],
            "passive": []
        },
        "fighter": {
            "high": [],
            "passive": []
        },
        "rogue": {
            "special": [],
            "high": [],
            "passive": []
        },
        "tank": {
            "special": [],
            "high": [],
            "passive": []
        },
        "wizard": {
            "special": [],
            "high": [],
            "passive": []
        },

    }}


for path, subdirs, files in os.walk(DATA):
    for name in files:
        file = (os.path.join(path, name).replace(
            DATA+"\\", "").replace("\\", "/"))
        file = file.split("/")
        if file[0] == "class":
            if file[3].endswith(".json"):
                # class powers being placed into class key
                powers["class"][file[1]][file[2]].append(
                    str(file[3].replace(".json", "")))
            else:
                # preventing double appending with primary & secondary powers
                if file[4] == "primary.json":
                    powers["class"][file[1]][file[2]].append(
                        str(file[3]))
        else:
            if str(file[1]) not in powers[file[0]]:
                powers[file[0]].append(str(file[1]).replace(".json", ""))

for path, subdirs, files in os.walk(os.path.join(RESOURCES + "/chill/textures/icons/")):
    for name in files:
        file = (os.path.join(path, name).replace(
            RESOURCES+"/chill/textures/icons/", "").replace("\\", "/"))
        file = file.split("/")
        if len(file) != 1 and "temp.txt" not in file:
            if file[0] == "class":
                print(file)
                if file[3].endswith(".png"):
                    # class powers being placed into class key
                    powers["class"][file[1]][file[2]].append(
                        str(file[3].replace(".png", "")))
            else:
                if str(file[1]) not in powers[file[0]]:
                    powers[file[0]].append(str(file[1]).replace(".png", ""))

file = open("C:\\Users\\Ice424\\curseforge\\minecraft\\Instances\\OriginsV5 - 1.21.1\\resourcepacks\\Origins-V5-Reasources\\powers.json", "w")
file.write(str(powers).replace("'", '"'))
file.close()
