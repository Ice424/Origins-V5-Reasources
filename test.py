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
def add_power(powers, category, entry, group=None, subcategory=None):
    """
    Adds a power entry to the JSON structure if it doesn't already exist.
    
    Args:
        powers (dict): The JSON structure.
        category (str): The main category ('high', 'low', or 'class').
        entry (dict): The new entry to add (e.g., {"name": "new_power", "predicate": 99}).
        group (str, optional): The group within 'class' (e.g., 'cleric').
        subcategory (str, optional): The specific subcategory within the group ('special', 'high', 'passive').
    """
    name = entry["name"].strip().lower()
    predicate = entry["predicate"]

    if category in powers:
        if group and category == "class":
            if group in powers["class"] and subcategory in powers["class"][group]:
                target_list = powers["class"][group][subcategory]
            else:
                print(f"Invalid group '{group}' or subcategory '{subcategory}' in class.")
                return
        else:
            target_list = powers[category]

        # Check for duplicates
        if any(item["name"].strip().lower() == name for item in target_list):
            print(f"Duplicate found: {name}")
            return

        # Add new entry
        target_list.append({"name": name, "predicate": predicate})
        print(f"Added: {name}")



# Adding to a top-level category
add_power(powers, "high", {"name": "new_power", "predicate": 99})

# Adding to a specific subcategory within "class"
add_power(powers, "class", {"name": "new_class_power", "predicate": 100}, group="cleric", subcategory="special")

# Attempting to add a duplicate
add_power(powers, "class", {"name": "new_class_power", "predicate": 101}, group="cleric", subcategory="special")

print(powers)
print(powers)