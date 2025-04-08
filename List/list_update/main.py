def smelt_ore(inventory):
    item = inventory[1]
    if item == "Iron Ore":
        inventory[1]= "Iron Bar"
    return inventory