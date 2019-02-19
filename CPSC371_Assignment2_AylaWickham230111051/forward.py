# Forward.py
# CPSC371
# Ayla Wickham
# 230111051

import time
import copy
import math

table = {
    1: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    2: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    3: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    4: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    5: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    6: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    7: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    8: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    9: {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9], 3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        4: [1, 2, 3, 4, 5, 6, 7, 8, 9], 5: [1, 2, 3, 4, 5, 6, 7, 8, 9], 6: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 8: [1, 2, 3, 4, 5, 6, 7, 8, 9], 9: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
}

class Forward:

    def __init__(self, filename):
        self.startTime = time.time()
        self.nodesVisited = 0
        self.grid = table
        self.setup(filename)
        self.changes = []
        self.start()

    # setup(filename)
    # inputs the known values into the grid from file
    def setup(self, filename):
        fn = open(filename, 'r')

        for lidx, line in enumerate(fn):
            for vidx, value in enumerate(line):
                if value == '\n' or int(value) == 0: continue
                self.insert((3*math.floor(lidx/3) + 1 + math.floor(vidx/3), 3*(lidx%3)+1+vidx%3, int(value)))

    # Main entry point of algorithm
    def start(self):
        solution = False
        while(not solution):
            solution = self.addChange()

        self.printOutput()


    def addChange(self):
        tNum, iNum = self.lowestChoice()
        if not tNum:
            return True
        elif len(self.grid[tNum][iNum]) == 0:
            self.grid = self.changes.pop()
            return
        elif len(self.grid[tNum][iNum]) == 1:
            self.insert((tNum, iNum, self.grid[tNum][iNum][0]))
            return
        value = self.grid[tNum][iNum][0]
        self.grid[tNum][iNum].remove(value)
        self.changes.append(copy.deepcopy(self.grid))

        self.insert((tNum, iNum, value))

    # Finds the index with fewest choices left
    def lowestChoice(self):
        length = 10
        tNum = 0
        iNum = 0

        for table in self.grid:
            for index in self.grid[table]:
                if isinstance(self.grid[table][index], list) and len(self.grid[table][index]) < length:
                    length = len(self.grid[table][index])
                    tNum = table
                    iNum = index

        return (tNum, iNum)

    # Inserts the value into given index
    def insert(self, data):
        self.nodesVisited += 1
        tNum, iNum, value = data
        self.grid[tNum][iNum] = value
        self.removeTable(data)
        self.removeRow(data)
        self.removeColumn(data)

    # Removes the given value from the remaining choices with in the table
    def removeTable(self, data):
        tNum, iNum, value = data
        for x in self.grid[tNum]:
            if isinstance(self.grid[tNum][x], list) and value in self.grid[tNum][x]: self.grid[tNum][x].remove(value)

    # Removes the given value from the remaining choices with in the row
    def removeRow(self, data):
        tNum, iNum, value = data

        htstart = math.floor((tNum-1)/3)*3+1
        histart = math.floor((iNum-1)/3)*3+1
        for x in range(htstart, htstart+3):
            for y in range(histart, histart+3):
                if isinstance(self.grid[x][y], list) and value in self.grid[x][y]: self.grid[x][y].remove(value)

    # Removes the given value from the remaingin choices with in the column
    def removeColumn(self, data):
        tNum, iNum, value = data

        vtstart = tNum%3

        for x in range(tNum%3, 10, 3):
            for y in range(iNum%3, 10, 3):
                if x < 1 or y < 1 : continue
                if isinstance(self.grid[x][y], list) and value in self.grid[x][y]: self.grid[x][y].remove(value)

    # Prints the grid
    def printDic(self):
        return self.printDc(self.grid)



    # Prints the changes list for debugging
    def printChanges(self):
        for dic, cand in self.changes:
            print("Dic in change: ")
            self.printDc(dic)
            print("Candidates: ", cand)


    # prints the given dictionary for debugging purposes
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


    # Prints the Output
    def printOutput(self):
        print("Solution: ")
        lst = self.printDic()
        lst2 = copy.deepcopy(lst)
        print("Nodes Visited: ",self.nodesVisited)
        print("Time Elapsed: ",time.time() - self.startTime)

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
