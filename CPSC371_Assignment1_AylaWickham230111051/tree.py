# Tree class
# Assignment 1
# CPSC371
# Ayla Wickham
# 230111051
from anytree import Node, RenderTree
import math
import sys

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

#Adds the lst to the visited list as we have now seen it
#Checks to see if it is goal state: if not adds the node to a list using the provided method
def notVisited(direction, node, lst):
    visited.add(lst)
    notChecked = Node(direction, parent = node, data = lst, depth = node.depth + 1)
    if lst == goal: return notChecked
    if mode == "BreathFirst" :
        checkList.append(notChecked)
    elif mode == "Manhattan":
        manhattan(notChecked)
        insert(notChecked)
    elif mode == "Tiles":
        tiles(notChecked)
        insert(notChecked)
    elif mode == "AStar":
        aStar(notChecked)
        insert(notChecked)

#Manhattan: calculates the Manhattan distance
def manhattan(node):
    cost = 0
    for indx, val in enumerate(node.data) :
        if val == 0 : continue
        distance = abs(indx - goal.index(val))
        cost += math.floor(distance/3) + distance%3
    node.cost = cost

#Calculates the number of tiles out of place
def tiles(node):
    cost = 0
    for indx, val in enumerate(node.data):
        if val == 0: continue
        if indx != goal.index(val): cost += 1

    node.cost = cost

#Calculates the cost using the Manhattan distance as a heuristic
def aStar(node):
    manhattan(node)
    node.cost += node.depth

#Inserts the node into the queue
def insert(node):
    inserted = False
    for indx, checkNode in enumerate(checkList):
        if checkNode.cost >= node.cost :
            checkList.insert(indx, node)
            inserted = True
            break

    if not inserted : checkList.append(node)

#Calculates the next state if 0 is moved up, down, left, or right.
#Then it checks to see if it is a new state. If it is it is added into the queue and visited list via notVisited()
def move(node):
    listcopy = list(node.data)
    index = listcopy.index(0)
    goal = None

    # move up
    if index > 2 :
        listcopy[index] = node.data[index-3]
        listcopy[index-3] = 0
        tuplecopy = tuple(listcopy)
        if tuplecopy not in visited:
            goal = notVisited("up", node, tuplecopy)
            if goal: return goal

    # move down
    if index < 6:
        listcopy = list(node.data)
        listcopy[index] = node.data[index+3]
        listcopy[index+3] = 0

        tuplecopy = tuple(listcopy)
        if tuplecopy not in visited:
            goal = notVisited("down", node, tuplecopy)
            if goal: return goal

    # move left
    if index % 3 != 0 :
        listcopy = list(node.data)
        listcopy[index] = node.data[index-1]
        listcopy[index-1] = 0

        tuplecopy = tuple(listcopy)
        if tuplecopy not in visited:
            goal = notVisited("left", node, tuplecopy)
            if goal: return goal

    # move right
    if index % 3 != 2 :
        listcopy = list(node.data)
        listcopy[index] = node.data[index+1]
        listcopy[index+1] = 0

        tuplecopy = tuple(listcopy)
        if tuplecopy not in visited:
            goal = notVisited("right", node, tuplecopy)
            if goal: return goal

    return goal

#Program starts here
args = sys.argv

#Gets file name for start states and the method used to search tree
filename = args[1]
mode = args[2]

writeFile = open(mode+"Results.txt", "w")

with open(filename) as file:

    for line in file:
        lst = tuple(int(x)for x in line if x != '\n')
        writeFile.write(str(lst))
        writeFile.write(": ")
        root = Node("root", data = lst, depth = 0)
        visited = set(root.data)
        checkList = [root]

        currentNode = None
        #Entry point for each start state
        while(checkList and not currentNode):
            currentNode = move(checkList.pop(0))

        writeFile.write(str(currentNode))
        writeFile.write("\n")
        print(currentNode)
