# Forward.py
# CPSC371
# Assignment 2
# Ayla Wickham
# 230111051

import copy
import math

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

    def __init__(self, filename):
        self.grid = [copy.deepcopy(table) for x in range(9)]
        self.changes = []
        self.setup(filename)
        self.start()

    def setup(self, filename):
        fn = open(filename, 'r')

        for lidx, line in enumerate(fn):
            for vidx, value in enumerate(line):
                if value == '\n' or int(value) == 0: continue
                data = (int(value), (3*math.floor(lidx/3) + math.floor(vidx/3))+1, (3*(lidx%3) + (vidx%3))+1)
                self.insert(data)
                # self.grid[int(value)-1][(3*math.floor(lidx/3) + math.floor(vidx/3))+1] = (3*(lidx%3) + (vidx%3))+1

    def start(self):
        changed = True
        #find number with least spots
        while(changed):
            changed = False
            for vidx, value in enumerate(self.grid):
                for table in value:
                    if isinstance(value[table], list):
                        if len(value[table]) == 1:
                            self.insert((vidx+1, table, value[table][0]))
                            changed = True

    def insert(self, data): #tNum, iNum, element):
        num, tNum, iNum = data
        change = (num, tNum, iNum, self.grid[num-1][tNum])
        self.changes.insert(0, change)
        tDict = self.grid[num-1]
        tDict[tNum] = iNum
        self.removeFromTable(data)


    def removeFromTable(self, data): #element, position):
        num, tNum, iNum = data
        eDic = self.grid[num-1]
        eDic[tNum] = iNum
        vStart = tNum % 3
        vList = [x for x in range(iNum%3, 10, 3)]


        #vertical removal
        for x in range(vStart, 10, 3):
            if x < 1 or not isinstance(eDic[x], list): continue
            eDic[x] = [y for y in eDic[x] if y not in vList]

        #Horizontal removal
        htStart = tNum-((tNum-1))%3
        hiStart = iNum-((iNum-1))%3
        hList = [x for x in range(hiStart, hiStart+3)]
        for x in range(htStart, htStart+3):
            if not isinstance(eDic[x], list): continue
            eDic[x] = [y for y in eDic[x] if y not in hList]

        #remove index from numbers
        for idx, dic in enumerate(self.grid):
            if idx == num-1 or not isinstance(dic[tNum], list): continue
            if iNum in dic[tNum]: dic[tNum].remove(iNum)


    def undoRemove(self):
        num, tNum, iNum, lst = self.changes.pop(0)
        eDic = self.grid[num-1]
        eDic[tNum] = lst
        vStart = tNum% 3
        vList = [x for x in range(iNum%3, 10, 3)]

        #Vertical undo
        for x in range(vStart, 10, 3):
            if not isinstance(eDic[x], list): eDic[x] = [eDix[x]] + vList
            eDic[x] = [y for y in range(1, 10) if y in eDic[x] or vList]

        #Horizontal undo
        htStart = tNum-((tNum-1))%3
        hiStart = iNum-((iNum-1))%3
        hList = [x for x in range(hiStart, hiStart+3)]
        for x in range(htStart, htStart+3):
            if not isinstance(eDic[x], list): eDix[x] = [eDic[x]] + hList
            eDic[x] = [y for y in range(1, 10) if y in eDic[x] or hList]

        #Index from numbers undo
        for idx, dic in enumerate(self.grid):
            if idx == num-1: continue
            if not isinstance(dic[tNum], list): dic[tNum] = [dic[tNum], iNum]
            dic[tNum].append(iNum)

    def printDic(self):
        for idx, dic in enumerate(self.grid):
            print(idx, ": ")
            print(dic)

    def printOutput(self):
        for idx, dic in enumerate(self.grid):
            for table in dic:
                


# forward = Forward()
# data = (2, 8, 9)
# forward.insert(data)
# forward.printDic()
# print("UNDO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# forward.undoRemove()
# forward.printDic()

# lst = [1,2 ,3 ,4]
# lst2 = [5, 6, 7]
# lst3 = lst.append(lst2)
# print(lst)
