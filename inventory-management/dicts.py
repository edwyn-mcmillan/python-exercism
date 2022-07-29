def create_inventory(items):
    return {item: items.count(item) for item in items}


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    inventory_tuple = [(key, value) for key, value in inventory.items() if inventory[key] > 0]
    return inventory_tuple
    