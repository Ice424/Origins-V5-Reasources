import os
import json
from pathlib import Path
os.chdir(Path(__file__).parents[2])

RESOURCES = os.path.abspath(
    "./resourcepacks/Origins-5E-Reasources/assets/")

DATA = os.path.abspath(
    "./saves/New World/datapacks/Origins-5E-Data/data/chill/powers")

MODEL = {
    "parent": "minecraft:item/handheld",
    "textures": {
        "layer0": ""
    }
}


def generate_json():
    predicate = 10
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
            if os.name == "nt":
                file = (os.path.join(path, name).replace(
                    DATA + "\\", "").replace("\\", "/"))
            else:
                file = (os.path.join(path, name).replace(DATA + "/", ""))
            file = file.split("/")

            if file[0] == "class":
                if file[3] != "tag.json" and file[3].endswith(".json"):
                    # class powers being placed into class key
                    powers["class"][file[1]][file[2]].append({
                        "name": str(file[3].replace(".json", "")),
                        "predicate": predicate
                    })
                    predicate += 1

                elif file[3] != "tag.json" and file[4] == "primary.json":
                    powers["class"][file[1]][file[2]].append({
                        "name": str(file[3]),
                        "predicate": predicate
                    })
                    predicate += 1

            elif str(file[1]) not in powers[file[0]]:
                powers[file[0]].append({
                    "name": str(file[1]).replace(".json", ""),
                    "predicate": predicate
                })
                predicate += 1

    for path, subdirs, files in os.walk(os.path.join(RESOURCES + "/chill/textures/icons/")):
        for name in files:
            file = (os.path.join(path, name).replace(
                RESOURCES+"/chill/textures/icons/", "").replace("\\", "/"))
            file = file.split("/")
            if len(file) != 1 and "temp.txt" not in file and file[0] == "class" and file[3].endswith(".png"):
                # class powers being placed into class key
                powers["class"][file[1]][file[2]].append({
                    "name": str(file[3].replace(".png", "")),
                    "predicate":  predicate
                })
                predicate += 1

    file = open("./resourcepacks/Origins-5E-Reasources/powers.json", "w")
    file.write(json.dumps(powers, indent=4))
    file.close()


def generate_models(path):
    file = open("./resourcepacks/Origins-5E-Reasources/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    def GetPowers(types):
        for power in powers[types]:
            power = power["name"]
            try:
                os.makedirs(os.path.join(path, types))
            except:
                pass

            file = open(os.path.join(path, types, power)+".json", "w")
            out = MODEL
            out["textures"]["layer0"] = "chill:icons/" + types + "/" + power
            file.write(json.dumps(out, indent=4))
            file.close()
    GetPowers("low")
    GetPowers("high")
    for classes in powers["class"]:
        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                power = power["name"]
                try:
                    os.makedirs(os.path.join(path, "class", classes, types))
                except:
                    pass
                out = MODEL
                out["textures"]["layer0"] = "chill:icons/class/" + \
                    types + "/" + power
                file = open(os.path.join(path, "class",
                            classes, types, power)+".json", "w")
                file.write(json.dumps(out, indent=4))
                file.close()


def generate_tags(path):
    file = open("./resourcepacks/Origins-5E-Reasources/powers.json", "r")
    powers = json.loads(file.read())
    file.close()
    tag = {
        "types": "origins:action_on_callback",
        "entity_action_gained": {
            "types": "origins:execute_command",
            "command": ""
        },
        "entity_action_lost": [],
        "hidden": True
    }
    out = tag
    for classes in powers["class"]:

        for types in powers["class"][classes]:
            out["entity_action_gained"]["command"] = "tag @s add " + classes
            for power in powers["class"][classes][types]:
                power = power["name"]
                out["entity_action_lost"].append({
                    "types": "origins:execute_command",
                    "command": "tag @s remove " + power
                })
            try:
                os.makedirs(os.path.join(path, "class", classes, "passive"))
            except:
                pass
        file = open(os.path.join(path, "class", classes,
                    "passive", "tag")+".json", "w")
        file.write(json.dumps(out, indent=4))
        file.close()
        out["entity_action_lost"] = []


def generate_predicates():
    file = open("./resourcepacks/Origins-5E-Reasources/powers.json", "r")
    powers = json.loads(file.read())
    file.close()
    out = []

    def GetPowers(types):
        for power in powers[types]:
            out.append({"predicate": {"custom_model_data": power["predicate"]},
                        "model": "chill:" + os.path.join(types, power["name"]).replace("\\", "/")})

    GetPowers("low")
    GetPowers("high")
    for classes in powers["class"]:

        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                out.append({"predicate": {"custom_model_data": power["predicate"]},
                            "model": "chill:" + os.path.join("class", classes, types).replace("\\", "/")})

    with open("./resourcepacks/Origins-5E-Reasources/assets/minecraft/models/item/stick.json", "r") as file:
        data = json.load(file)

    for override in out:
        if override in data["overrides"]:
            data["overrides"].remove(override)
    
    for override in out:
        data["overrides"].append(override)
    
    with open("./resourcepacks/Origins-5E-Reasources/assets/minecraft/models/item/stick.json", "w") as file:
        json.dump(data, file, indent=4)


generate_json()

generate_models(
    "./resourcepacks/Origins-5E-Reasources/assets/chill/models/icons/")

generate_tags(DATA)

generate_predicates()
