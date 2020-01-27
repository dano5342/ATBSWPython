inv = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

        print("Inventory:")

        items = 0
        for k, v in inventory.items():
            print( k , ": ", v)
            items += v
        print("\n Total number of items: ", items)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
