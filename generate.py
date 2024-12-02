import os
from pathlib import Path
os.chdir(Path(__file__).parents[2])
RESOURCES = os.path.abspath("./resourcepacks/Origins-V5Resources/assets")
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
        file = (os.path.join(path, name).replace("/home/elliotd/.local/share/ModrinthApp/profiles/OriginsV5/saves/New World/datapacks/Origins-V5-Data/data/chill/powers/",""))
        file = file.split("/")
        print(file)
        if file[0] == "class":
            powers["class"][file[1]].append(str(file[2:]))
        else:
            powers[file[0]].append(str(file[1]))

file = open("/home/elliotd/.local/share/ModrinthApp/profiles/OriginsV5/resourcepacks/Origins-V5-Reasources/powers.json", "w")
file.write(str(powers))
file.close()