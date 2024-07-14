class ThroneInheritance:
    def __init__(self, kingName: str):
        # This is equivalent to the root node in a tree.
        self.kingName = kingName
        # Since we know that all family members' names are distinct,
        # (no two names are the same), we can use a hash table.
        # Anyone who has descendants is a "key" in this hash table.
        self.ht = {kingName: []}
        # Keep track of who dies.
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        # Updates the family tree.
        if parentName not in self.ht:
            self.ht[parentName] = []
        self.ht[parentName].append(childName)

    def death(self, name: str) -> None:
        # Updates who dies.
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []
        stack = [self.kingName]
        name = ""
        # Traverses the family tree.
        while len(stack) > 0:
            # Get the current name.
            name = stack.pop()
            # Add the person to the inheritance order if
            # he or she is still alive.
            if name not in self.deaths:
                inheritanceOrder.append(name)
            # Add the person's descendants to the stack in
            # reverse order if they exist.
            if name in self.ht:
                for i in range(len(self.ht[name])-1, -1, -1):
                    stack.append(self.ht[name][i])
        return inheritanceOrder