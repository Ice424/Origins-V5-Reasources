import os
from pathlib import Path
os.chdir(Path(__file__).parents[2])
RESOURCES = os.path.abspath("./resourcepacks/Origins-V5-Reasources/assets/")
DATA = os.path.abspath(
    "./saves/New World/datapacks/Origins-V5-Data/data/chill/powers")

#
powers = {
    "high": [],
    "low": [],
    "class": {
        "cleric": [],
        "druid": [],
        "fighter": [],
        "rogue": [],
        "tank": [],
        "wizard": []

    }}


for path, subdirs, files in os.walk(DATA):
    for name in files:
        file = (os.path.join(path, name).replace(DATA+"/", ""))
        file = file.split("/")

        if file[0] == "class":
            if file[3].endswith(".json"):
                #class powers being placed into class key
                powers["class"][file[1]].append(
                    str(file[3].replace(".json", "")))
            else:
                #preventing double appending with primary & secondary powers
                if file[4] == "primary.json":
                    powers["class"][file[1]].append(
                        str(file[3]))

        else:
            #General duplicate prevention for low and high powers as they appear multiple times (different levels)
            if str(file[1]) not in powers[file[0]]: 
                powers[file[0]].append(str(file[1]).replace(".json", ""))

for path, subdirs, files in os.walk(os.path.join(RESOURCES+ "/chill/textures/icons/")):
    for name in files:
        print(file)
        file = (os.path.join(path, name).replace(RESOURCES+"/chill/textures/icons/", ""))
        file = file.split("/")
        

file = open("/home/elliotd/.local/share/ModrinthApp/profiles/OriginsV5/resourcepacks/Origins-V5-Reasources/powers.json", "w")
file.write(str(powers).replace("'", '"'))
file.close()