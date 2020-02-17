'''
EightPuzzleWithManhattan.py
created by Wayne Wang
UWNetID: wyf9686
Student number: 1664873
Date: Oct 18, 2019

Assignment 3, in CSE 415, Autumn 2019.

This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
'''

from EightPuzzle import *

def h(s):
  dist = 0
  for i in range(3):  # row index
    for j in range(3): # column index
        if s.b[i][j] != 0:
            value = s.b[i][j]
            row = int(value / 3) # get the row index given value supposes to have
            col = value % 3 # get the column index given value supposes to have
            dist = dist + abs(row - i) + abs(col - j) # adding up all distances
  return dist
