# Forward.py
# CPSC371
# Assignment 2
# Ayla Wickham
# 230111051

import copy

table = {
    1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    2: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    4: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    5: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    7: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    8: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

class Forward:

    def __init__(self):
        self.grid = [copy.deepcopy(table) for x in range(9)]


    def insert(self, position, element): #tNum, iNum, element):
        tNum, iNum = position
        tDict = self.grid[tNum-1]
        tDict[iNum] = element



    # def remove(self, position, element):
    #     #Removes element from rest of table
    #     for x, y in tDict.items():
    #         if isinstance(y, list) and element in y: y.remove(element)

        #Removes element from rest of corresponding grid

    def removeFromTable(self, position, element, vertical) :
        tNum, iNum = position
        tStart = (tNum + 1) % 3
        iStart = (iNum+1) % 3
        if vertical:
            for x in range(tStart-1, 9, 3):
                if x < 0 : continue
                grid[x]
        tDict = grid[tNum]
        for x in iNum:
            if isinstance(tDict[x], list) and element in tDict[x]: tDict[x].remove(element)

forward = Forward()
position = (5, 5)
forward.insert(position, 5)
print(forward.grid[4])
