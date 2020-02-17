'''
EightPuzzleWithHamming.py
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
  num = 0
  for i in range(3): # Row index
    for j in range(3): # Column index
      if s.b[i][j] != 0: # exclude the blank spot
        if s.b[i][j] != 3 * i + j:
          num += 1
  return num
