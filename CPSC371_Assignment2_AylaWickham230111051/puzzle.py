# Sudoku puzzle
# Assignment 2
# CPSC 371
# Ayla Wickham
# 230111051

import sys
import forward

args = sys.argv
filename = args[1]

#get first puzzle

frwrd = forward.Forward(filename)
frwrd.printDic()
# with open(filename) as file:
    # for line in file:
        # print(line)
