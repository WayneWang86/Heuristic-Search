''' Rubik2Cube.py Modified from EightPuzzle.py,
Created by
Wayne Wang
Date: Oct 11, 2019

Assignment 2, in CSE 415, Autumn 2019.

'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Rubik's Cube 2*2"
PROBLEM_VERSION = "0.2"
PROBLEM_AUTHORS = ['Wayne Wang']
PROBLEM_CREATION_DATE = "18-OCT-2019"
PROBLEM_DESC=\
'''This formulation of the Rubik's 2*2 cube uses generic
Python 3 constructs and has been tested with Python 3.6.
'''
#</METADATA>


# <COMMON_DATA>
# </COMMON_DATA>

# <COMMON_CODE>
# use numbers to represent different side of the cube
F = 0;
B = 1;
U = 2;
D = 3;
L = 4;
R = 5;

sides_names = {
    "F": "Front",
    "B": "Back",
    "U": "Upper",
    "D": "Down",
    "L": "Left",
    "R": "right"
}

class State:
    def __init__(self, b):
        self.b = b

    def __eq__(self, s2):
        for i in range(6): # 6 sides
            for j in range(4): # 4 positions on each side
                if self.b[i][j] != s2.b[i][j]:
                    return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        return str(self.b)

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        news.b = [row[:] for row in self.b]
        return news

    def can_move(self, side):
        # always return true since there is no limitation to which side to rotate
        return True

    def move(self, side):
        '''Assuming it's legal to make the move, this computes
           the new state resulting from moving a tile in the
           given direction, into the void.'''
        news = self.copy()  # start with a deep copy.
        b = news.b
        if side == 'F':
            # change on the front side
            fr_up_left = b[F][0]
            b[F][0] = b[F][2]
            b[F][1] = fr_up_left
            b[F][2] = b[F][3]
            b[F][3] = b[F][1]
            # change on Upper, Down, Left and Right sides
            up_low_left = b[U][2]
            up_low_right = b[U][3]
            b[U][2] = b[L][3]
            b[U][3] = b[L][1]
            b[L][3] = b[D][1]
            b[L][1] = b[D][0]
            b[D][1] = b[R][0]
            b[D][0] = b[R][2]
            b[R][0] = up_low_left
            b[R][2] = up_low_right

        elif side == 'U':
            # Change on the Upper side
            up_up_left= b[U][0]
            b[U][0] = b[U][2]
            b[U][1] = up_up_left
            b[U][2] = b[U][3]
            b[U][3] = b[U][1]
            # Change on the Front, Back, Left and Right Side
            ba_low_left = b[B][2]
            ba_low_right = b[B][3]
            b[B][2] = b[L][1]
            b[B][3] = b[L][0]
            b[L][1] = b[F][1]
            b[L][0] = b[F][0]
            b[F][1] = b[R][1]
            b[F][0] = b[R][0]
            b[R][1] = ba_low_left
            b[R][0] = ba_low_right

        elif side == 'B':
            # Change on the Back side
            ba_up_left = b[B][0]
            b[B][0] = b[B][2]
            b[B][1] = ba_up_left
            b[B][2] = b[B][3]
            b[B][3] = b[B][1]
            # Change on the Up, Down, Left and Right Side
            do_low_left = b[D][2]
            do_low_right = b[D][3]
            b[D][2] = b[L][0]
            b[D][3] = b[L][2]
            b[L][0] = b[U][1]
            b[L][2] = b[U][0]
            b[U][1] = b[R][3]
            b[U][0] = b[R][1]
            b[R][3] = do_low_left
            b[R][1] = do_low_right

        elif side == 'D':
            # Change on the Down side
            do_up_left = b[D][0]
            b[D][0] = b[D][2]
            b[D][1] = do_up_left
            b[D][2] = b[D][3]
            b[D][3] = b[D][1]
            # Change on the Front, Back, Left and Right Side
            fr_low_left = b[F][2]
            fr_low_right = b[F][3]
            b[F][2] = b[L][2]
            b[F][3] = b[L][3]
            b[L][2] = b[B][1]
            b[L][3] = b[B][0]
            b[B][1] = b[R][2]
            b[B][0] = b[R][3]
            b[R][2] = fr_low_left
            b[R][3] = fr_low_right

        elif side == 'L':
            # Change on the Left side
            le_up_left = b[L][0]
            b[L][0] = b[L][2]
            b[L][1] = le_up_left
            b[L][2] = b[L][3]
            b[L][3] = b[L][1]
            # Change on the Front, Back, Upper and Down Side
            up_up_left = b[U][0]
            up_low_left = b[U][2]
            b[U][0] = b[B][0]
            b[U][2] = b[B][2]
            b[B][0] = b[D][0]
            b[B][2] = b[D][2]
            b[D][0] = b[F][0]
            b[D][2] = b[F][2]
            b[F][0] = up_up_left
            b[F][2] = up_low_left

        elif side == 'R':
            # Change on the Right side
            ri_up_left = b[R][0]
            b[R][0] = b[R][2]
            b[R][1] = ri_up_left
            b[R][2] = b[R][3]
            b[R][3] = b[R][1]
            # Change on the Front, Back, Upper and Down Side
            up_low_right = b[U][3]
            up_up_right = b[B][1]
            b[U][3] = b[F][3]
            b[U][1] = b[F][1]
            b[F][3] = b[D][3]
            b[F][1] = b[D][1]
            b[D][3] = b[B][3]
            b[D][1] = b[B][1]
            b[B][3] = up_low_right
            b[B][1] = up_up_right
        return news  # return new state

    def edge_distance(self, s2):
        return 1.0  # Warning, this is only correct when
        # self and s2 are neighboring states.
        # We assume that is the case.  This method is
        # provided so that problems having all move costs equal to
        # don't have to be handled as a special case in the algorithms.


def goal_test(s):
    '''If all the b values are in order, then s is a goal state.'''
    for i in range(6): # Each side of the cube
        color = s.b[i][0] # The color on the upper left position
        for j in range(1, 4): # Check if the rest position has the same color
            if (s.b[i][j] != color):
                return False
    return True

def goal_message(s):
    return "You've got the cube to the right state. Great!"

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)
# </COMMON_CODE>

# <INITIAL_STATE>
# Use default, but override if new value supplied
# by the user on the command line.

try:
    import sys
    init_state_string = sys.argv[2]
    print("Initial state as given on the command line: " + init_state_string)
    init_state_list = eval(init_state_string)
except:
    # 0, 1, 2, 3, 4, 5 represent 6 different colors
    # each array represents a side, each index with sub-array represents a
    # position on the side: 0 -> upper left; 1 -> upper right; 2 -> lower left; 3 -> lower right

    init_state_list = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 4, 4], [3, 3, 5, 5], [3, 2, 3, 2], [5, 4, 5, 4]]
    # init_state_list = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 5, 5], [2, 2, 5, 5], [3, 4, 3, 4], [3, 4, 3, 4]]

    # OTHER TEST:
    # init_state_list = [[0, 2, 0, 5], [1, 2, 1, 5], [2, 0, 5, 0], [2, 1, 5, 1], [3, 4, 3, 4], [3, 3, 4, 4]]

    print("Using default initial state list: " + str(init_state_list))
    print(" (To use a specific initial state, enter it on the command line, e.g.,")

CREATE_INITIAL_STATE = lambda: State(init_state_list)
# </INITIAL_STATE>

# <OPERATORS>
# 6 Direction: F (front), B (back), U (upper), D (down-side), L (left), R (right)
sides = ["F", "B", "U", "D", "L", "R"]

OPERATORS = [Operator("Rotate " + sides_names[side] + " side clockwise",
                      lambda s, side1 = side: s.can_move(side1),
                      # The default value construct is needed
                      # here to capture the value of dir
                      # in each iteration of the list comp. iteration.
                      lambda s, side1 = side: s.move(side1))
             for side in sides]
# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>
