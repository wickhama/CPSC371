# Sudoku puzzle
# Assignment 2
# CPSC 371
# Ayla Wickham
# 230111051

import sys
import forward
import backtracking

args = sys.argv
filename = args[2]
method = args[1]

if "Forward" == method: forward.Forward(filename)
else: backtracking.Backtracking(filename)
