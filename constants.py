from enum import Enum

P_STRAIGHT = 0.8
P_LEFT = 0.1
P_RIGHT = 0.1

R_WHITE = -0.05
R_GREEN = 1
R_BROWN = -1

DISCOUNT = 0.99
DIFF_THRESHOLD = 0.001

ROWS = 6
COLS = 6

START_COORDS = (2, 2)

# anticlockwise
class Actions(Enum):
    UP = 0
    RIGHT = 90
    DOWN = 180
    LEFT = 270
    NONE = -1
    def prev(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) - 1
        if index < 0:
            index = len(members)-2
        return members[index]

    def next(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members) - 1:
            index = 0
        return members[index]
   

# up => 1 
# class States(Enum):
#     WHITE = 1
#     GREEN = 2
#     BROWN = 3

class States(Enum):
    WALL = 0, 0
    WHITE = 1, -0.05
    GREEN = 2, 1
    BROWN = 3, -1
    SUPERGREEN = 4, 3

    def __new__(cls, value, reward):
        member = object.__new__(cls)
        member._value_ = value
        member.reward = float(reward)
        return member

    def _int__(self):
        return self.value