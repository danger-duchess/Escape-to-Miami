# Escape to Miami
#
class Inventory:
    def __init__(self):
        self._inv = {}
        self._inv_amount = 0
        self._max_amount = 5

    # use 2 variables to get item
    def getInventory(self):
        return self._inv_amount, self._inv

    def expandInventory(self, n):
        self._max_amount += n

    def addItem(self, item):
        if self._inv_amount < self._max_amount:
            if item in self._inv:
                self._inv[item] += 1
            else:
                self._inv[item] = 1
            self._inv_amount += 1
            return True
        else:
            return False

    def useItem(self, item):
        if self._inv_amount == 0:
            return False
        else:
            if item in self._inv:
                self._inv[item] -= 1
                self._inv_amount -= 1
                if self._inv[item] == 0:
                    del self._inv[item]
                return True
            else:
                return False

    # empties inventory on new game
    def emptyInv(self):
        self._inv.clear()

# short test to see if all/most functions of inventory work
if __name__ == "__main__":
    inventory = Inventory()
    print(inventory.addItem("Gas Can"))
    print(inventory.addItem("Snickers"))
    print(inventory.addItem("Gas Can"))
    print(inventory.addItem("A Whole ass Alligator"))
    print(inventory.addItem(3))
    if inventory.addItem("Chimken Nug") is False:
        print(inventory.useItem("Snickers"))
        print(inventory.addItem("Chimken Nug"))
    print(inventory.getInventory())
    inventory.expandInventory(1)
    print(inventory.addItem("More Chimken Nug"))
    print(inventory.getInventory())
    print(inventory.addItem("Gun"))
    print(inventory.useItem("God"))
    print(inventory.useItem("Chimken Nug"))
    print(inventory.useItem("Gas Can"))
    print(inventory.getInventory())
