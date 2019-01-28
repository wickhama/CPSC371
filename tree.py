# Tree class
# Assignment 1
# CPSC371
# Ayla Wickham
# 230111051

class Tree :
    def __init__(self, list, children = None):
        self.list = list
        self.children = []
        self.parent = parent

    def addChild(child):
        children.append(child)
        child.parent = this

    def find(list):
        if self.list is list : return list
        for child in self.children:
            n = find(list)
            if n: return n
        return None

    def __str__():
        return str(self.list)

print("Goodbye")
root = Tree([1, 2, 3])
child = Tree([0, 1, 2])
child1 = Tree([2, 1, 3])
child2 = Tree([1, 2, 4])
root.addChild(child)
root.addChild(child1)
child1.addChild(child2)

print(root.find([1, 2, 4]))
print("Hello")
