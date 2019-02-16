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
        self.tAffected = []    #List of Tables Affected by insert
        self.setup(filename)
        self.tAffected.clear()
        self.changes.clear()    #this is a start point if it has to go back before this point, initial state is unsolvable
        self.start2()

    def setup(self, filename):
        fn = open(filename, 'r')

        #Input numbers from file into proper dictionary positions
        for lidx, line in enumerate(fn):
            for vidx, value in enumerate(line):
                if value == '\n' or int(value) == 0: continue
                data = (int(value), (3*math.floor(lidx/3) + math.floor(vidx/3))+1, (3*(lidx%3) + (vidx%3))+1)
                self.insert(data)

        #Input all definately know postions (ie if there is only one choice for position x)
        for vidx, value in enumerate(self.grid):
            for table in value:
                if not isinstance(value[table], list): continue
                if len(value[table]) == 1:
                    self.insert((vidx+1, table, value[table][0]))

    def checkAffected(self):
        anyAffected = False
        while(self.tAffected):
            anyAffected = True
            num, table = self.tAffected.pop(0)
            # self.printDic()
            # print(num, table)
            if isinstance(self.grid[num-1][table], list) and len(self.grid[num-1][table]) == 1: self.insert((num, table, self.grid[num-1].get(table)[0]))

        return anyAffected

    def start2(self):
        affected = True
        while(affected):
            self.checkSmallChoice()
            self.printDic()
            print(self.tAffected)
            affected = self.checkAffected()


    def checkSmallChoice(self):
        candidate = []
        #Find value with least # of choices
        for didx, dic in enumerate(self.grid):
            for table in dic:
                if isinstance(dic[table], list):
                    if not candidate or len(dic[table]) < len(candidate[2]):
                        candidate = [didx+1, table, dic[table]]
        print(candidate)
        self.insert((candidate[0], candidate[1], candidate[2][0]))

    def start(self):
        # changed = True
        # obvious = True

        #find number with least spots
        # while(changed or obvious):
        changed = False
        obvious = False
        candidate = []
        for vidx, value in enumerate(self.grid):
            for table in value:
                if not isinstance(value[table], list): continue
                print(vidx+1, table, value[table])
                if len(value[table]) == 1:
                    self.insert((vidx+1, table, value[table][0]))
                    if not changed : changed = True
                elif not candidate or len(value[table]) < len(candidate[2]):
                    candidate = [vidx+1, table, value[table]]

        print(changed)
        #Add smalled value if it wasn't a single value(ie make a choice)
        if not changed:
            print(insert(candidate[0], candidate[1], candidate[2][0]))
                    # if not obvious: obvious = True
                    # if not obvious and (not candidate or len(value[table]) < len(candidate[2])):
                        # candidate = [vidx+1, table, value[table]]
                        # changed = True

            # if not obvious and changed:
            #     data = (candidate[0], candidate[1], candidate[2][0])
            #     self.insert(data)


    def insert(self, data):
        num, tNum, iNum = data
        change = (num, tNum, iNum, self.grid[num-1][tNum])
        self.changes.insert(0, change)
        tDict = self.grid[num-1]
        tDict[tNum] = int(iNum)
        self.removeFromTable(data)
        # if not self.removeFromTable(data):
            # self.undoMove()
            # self.printDic()
            # return False
        # return True



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
            # print("Vertical: ", (num, x))
            self.tAffected.append((num, x))
            if not eDic[x]:
                self.undoMove()
                return

        #Horizontal removal
        htStart = tNum-((tNum-1))%3
        hiStart = iNum-((iNum-1))%3
        hList = [x for x in range(hiStart, hiStart+3)]
        for x in range(htStart, htStart+3):
            if not isinstance(eDic[x], list): continue
            eDic[x] = [y for y in eDic[x] if y not in hList]
            # print("Horizontal: ", (num, x))
            self.tAffected.append((num, x))
            if not eDic[x]: 
                self.undoMove()
                return

        #remove index from numbers
        for idx, dic in enumerate(self.grid):
            # print("Numbers: ",idx, num-1)
            if idx == num-1 or not isinstance(dic[tNum], list): continue
            if iNum in dic[tNum]:
                dic[tNum].remove(iNum)
                # print("Numbers: ", (idx+1, tNum))
                self.tAffected.append((idx+1, tNum))
            if not dic[tNum]: 
                self.undoMove
                return



    def undoMove(self):
        num, tNum, iNum, lst = self.changes.pop(0)

        #if insert was a single choice then we need to go back further
        if len(lst) < 2 :
            self.undoMove()
            return

        eDic = self.grid[num-1]
        eDic[tNum] = lst[1:]
        vStart = tNum% 3
        vList = [x for x in range(iNum%3, 10, 3)]

        #Vertical undo
        #TODO Check for conflicting numbers!
        for x in range(vStart, 10, 3):
            if x < 1: continue
            if not isinstance(eDic[x], list): eDic[x] = [eDic[x]] + vList
            eDic[x] = [y for y in range(1, 10) if y in eDic[x] or vList]

        #Horizontal undo
        htStart = tNum-((tNum-1))%3
        hiStart = iNum-((iNum-1))%3
        hList = [x for x in range(hiStart, hiStart+3)]
        for x in range(htStart, htStart+3):
            if x < 1: continue
            if not isinstance(eDic[x], list): eDic[x] = [eDic[x]] + hList
            eDic[x] = [y for y in range(1, 10) if y in eDic[x] or hList]

        #Index from numbers undo
        for idx, dic in enumerate(self.grid):
            if idx == num-1: continue
            if not isinstance(dic[tNum], list): dic[tNum] = [dic[tNum], iNum]
            dic[tNum].append(iNum)

        #insert next choice
        self.insert((num, tNum, lst[1]))#eDic[tNum][0]))

    def printDic(self):
        for idx, dic in enumerate(self.grid):
            print(idx, ": ")
            print(dic)

    def printOutput(self):
        lst = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],]

        for idx, dic in enumerate(self.grid):
            for table in dic:
                lst[3*math.floor((table-1)/3) + math.floor((dic[table]-1)/3)][3*((table-1) % 3) + (dic[table]-1) % 3] = idx+1

        for line in lst:
            print(line)

