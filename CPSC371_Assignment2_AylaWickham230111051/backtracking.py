# Assignment 2
# CPSC 371
# Ayla Wickham
# 230111051

import time
import math
import copy


table = {
    1: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    2: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    3: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    4: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    5: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    6: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    7: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    8: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
    9: {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0
    },
}

class Backtracking:

    def __init__(self, filename):
        self.startTime = time.time()
        self.nodesVisited = 0
        self.grid = table
        self.setup(filename)
        self.changes = []
        self.start()

    # Adds the known values from the file into the appropriate index in the grid
    def setup(self, filename):
        fn = open(filename, 'r')

        for lidx, line in enumerate(fn):
            for vidx, value in enumerate(line):
                if value == '\n' or int(value) == 0: continue
                self.grid[3*math.floor(lidx/3) + 1 + math.floor(vidx/3)][3*(lidx%3)+1+vidx%3] = int(value)

    # Main entry point for the algorithm
    def start(self):
        sFound = False

        while(not sFound):
            sFound = self.insert()

        self.printOutput()

    # Inserts the next valid choice for the next position containing a 0
    def insert(self):
        zPos = self.getZero()
        if not zPos:
            return True #No more positions to check

        table, index = zPos
        candidates = self.findChoices((table, index, 0))

        if not candidates:
            change = self.changes.pop()
            self.grid = copy.deepcopy(change[0])
            candidates = change[1]
            table, index = self.getZero()


        if len(candidates) > 1: self.changes.append((copy.deepcopy(self.grid), candidates[1:]))
        self.grid[table][index] = candidates[0]

        self.nodesVisited += 1

    # Gets the index of the next 0
    def getZero(self):
        for table in self.grid:
            for position in self.grid[table]:
                if self.grid[table][position] == 0: return (table, position)



    # Calculates a list of valid choices for index given
    def findChoices(self, data):
        table, index, value = data
        lst = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        lst.difference_update(self.checkTable(data))
        lst.difference_update(self.checkRow(data))
        lst.difference_update(self.checkColumn(data))

        return list(lst)

    # Checks for valid choices with in table 
    def checkTable(self, data):
        tNum, index, value = data  # Do I need all values for everything?
        lst = []
        table = self.grid[tNum]
        for position in table:
            if table[position] == 0: continue
            lst.append(table[position])

        return lst

    # Checks for valid choices with in row
    def checkRow(self, data):
        tNum, index, value = data
        lst = []
        htstart = math.floor((tNum-1)/3)*3+1
        histart = math.floor((index-1)/3)*3+1
        for x in range(htstart, htstart+3):
            for y in range(histart, histart+3):
                if self.grid[x][y] == 0: continue
                lst.append(self.grid[x][y])

        return lst

    # Checks for valid choices with in column
    def checkColumn(self, data):
        tNum, index, value = data
        lst = []
        vtstart = tNum%3

        for x in range(tNum%3, 10, 3):
            for y in range(index%3, 10, 3):
                if x < 1 or y < 1 or self.grid[x][y] == 0: continue
                lst.append(self.grid[x][y])

        return lst

    # Prints the grid
    def printDic(self):
        return self.printDc(self.grid)


    # Prints the provided dictionary for debugging purposes
    def printDc(self, dic):
        lst = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for table in dic:
            for position in dic[table]:
                lst[3*math.floor((table-1)/3)+math.floor((position-1)/3)][3*((table-1)%3)+(position-1)%3] = dic[table][position]

        for line in lst:
            print(line)

        return lst


    # Prints the Changes list for debugging purposes
    def printChanges(self):
        for dic, cand in self.changes:
            print("Dic in change: ")
            self.printDc(dic)
            print("Candidates: ", cand)

    # Prints the Output
    def printOutput(self):
        print("Output: ")
        lst = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],]

        lst2 = copy.deepcopy(lst)
        lst = self.printDic()



        correct = False
        #checks if lines are correct
        for idx, line in enumerate(lst):
            correct = all(elem in line for elem in range(1, 10))
            if not correct:
                print(correct, " horizontal: ", idx, ": ", line)

            index = 0
            for num in line:
                lst2[index][idx] = num
                index = index + 1

        for idx, line in enumerate(lst2):
            correct = all(elem in line for elem in range(1, 10))
            if not correct:
                print(correct, " vertical: ", idx, ": ", line)

        print("Time Elapsed: ",time.time() - self.startTime)
        print("Nodes Visited: ", self.nodesVisited)
